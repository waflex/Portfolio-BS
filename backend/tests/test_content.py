"""
Tests de extremo a extremo para los endpoints de contenido
(proyectos, experiencia laboral, docencia).
"""

import pytest
from uuid import uuid4
from datetime import datetime, timezone

from sqlalchemy import select

from app.models import Project, WorkHistory, TeachingHistory
from app.schemas import TechnologyItem


# ── Helpers ──────────────────────────────────────────────────────────────────

NOW = datetime.now(timezone.utc)
TECH_REACT = TechnologyItem(name="React", icon="devicon-react-original", color="text-cyan-400")
TECH_NODE = TechnologyItem(name="Node.js", icon="devicon-nodejs-plain", color="text-green-500")


async def insert_project(db, **overrides):
    defaults = dict(
        title="Test Project", description="A test project", github="https://github.com/test",
        technologies=[TECH_REACT.model_dump()], sort_order=0, active=True,
        created_at=NOW, updated_at=NOW,
    )
    defaults.update(overrides)
    p = Project(**defaults)
    db.add(p)
    await db.commit()
    await db.refresh(p)
    return p


async def insert_work(db, **overrides):
    defaults = dict(
        title="Test Job", company="Test Co", period="2020-2024",
        description="A test job", technologies=[TECH_NODE.model_dump()],
        achievements=["Achievement 1"], sort_order=0, active=True,
        created_at=NOW, updated_at=NOW,
    )
    defaults.update(overrides)
    w = WorkHistory(**defaults)
    db.add(w)
    await db.commit()
    await db.refresh(w)
    return w


async def insert_teaching(db, **overrides):
    defaults = dict(
        title="Test Teacher", company="Test Institute", period="2023-2024",
        description="A test teaching", technologies=[TECH_REACT.model_dump()],
        activities=["Activity 1"], sort_order=0, active=True,
        created_at=NOW, updated_at=NOW,
    )
    defaults.update(overrides)
    t = TeachingHistory(**defaults)
    db.add(t)
    await db.commit()
    await db.refresh(t)
    return t


# ── GET /api/projects ────────────────────────────────────────────────────────

class TestListProjects:
    async def test_empty(self, client):
        resp = await client.get("/api/projects")
        assert resp.status_code == 200
        assert resp.json() == []

    async def test_returns_active_only(self, client, db_session):
        await insert_project(db_session, title="Active", active=True)
        await insert_project(db_session, title="Inactive", active=False)

        resp = await client.get("/api/projects")
        data = resp.json()
        assert len(data) == 1
        assert data[0]["title"] == "Active"

    async def test_ordered_by_sort_order(self, client, db_session):
        await insert_project(db_session, title="Second", sort_order=1)
        await insert_project(db_session, title="First", sort_order=0)

        resp = await client.get("/api/projects")
        titles = [p["title"] for p in resp.json()]
        assert titles == ["First", "Second"]

    async def test_returns_full_schema(self, client, db_session):
        p = await insert_project(db_session)
        resp = await client.get("/api/projects")
        data = resp.json()[0]
        assert data["id"] == str(p.id)
        assert data["title"] == "Test Project"
        assert data["technologies"][0]["name"] == "React"
        assert "created_at" in data
        assert "updated_at" in data


# ── GET /api/work-history ────────────────────────────────────────────────────

class TestListWorkHistory:
    async def test_empty(self, client):
        resp = await client.get("/api/work-history")
        assert resp.status_code == 200
        assert resp.json() == []

    async def test_returns_active_only(self, client, db_session):
        await insert_work(db_session, title="Active", active=True)
        await insert_work(db_session, title="Inactive", active=False)

        resp = await client.get("/api/work-history")
        assert len(resp.json()) == 1

    async def test_returns_achievements(self, client, db_session):
        await insert_work(db_session)
        resp = await client.get("/api/work-history")
        assert resp.json()[0]["achievements"] == ["Achievement 1"]


# ── GET /api/teaching ────────────────────────────────────────────────────────

class TestListTeaching:
    async def test_empty(self, client):
        resp = await client.get("/api/teaching")
        assert resp.status_code == 200
        assert resp.json() == []

    async def test_returns_active_only(self, client, db_session):
        await insert_teaching(db_session, title="Active", active=True)
        await insert_teaching(db_session, title="Inactive", active=False)

        resp = await client.get("/api/teaching")
        assert len(resp.json()) == 1

    async def test_returns_activities(self, client, db_session):
        await insert_teaching(db_session)
        resp = await client.get("/api/teaching")
        assert resp.json()[0]["activities"] == ["Activity 1"]


# ── Admin CRUD: Projects ─────────────────────────────────────────────────────

class TestAdminProjects:
    async def test_create_project(self, client, admin_headers):
        payload = {
            "title": "New Project",
            "description": "Brand new project",
            "github": "https://github.com/new",
            "technologies": [{"name": "Vue", "icon": "devicon-vuejs-plain", "color": "text-green-400"}],
        }
        resp = await client.post("/api/admin/projects", json=payload, headers=admin_headers)
        assert resp.status_code == 201
        data = resp.json()
        assert data["title"] == "New Project"
        assert data["technologies"][0]["name"] == "Vue"
        assert data["active"] is True

    async def test_create_requires_auth(self, client):
        resp = await client.post("/api/admin/projects", json={"title": "X", "description": "Y", "github": "https://x.com"})
        # Router-level Depends returns 403 vs endpoint-level 401
        assert resp.status_code in (401, 403)

    async def test_update_project(self, client, db_session, admin_headers):
        p = await insert_project(db_session)
        resp = await client.put(f"/api/admin/projects/{p.id}", json={"title": "Updated"}, headers=admin_headers)
        assert resp.status_code == 200
        assert resp.json()["title"] == "Updated"

    async def test_update_not_found(self, client, admin_headers):
        resp = await client.put(f"/api/admin/projects/{uuid4()}", json={"title": "Nope"}, headers=admin_headers)
        assert resp.status_code == 404

    async def test_delete_project(self, client, db_session, admin_headers):
        p = await insert_project(db_session)
        resp = await client.delete(f"/api/admin/projects/{p.id}", headers=admin_headers)
        assert resp.status_code == 200

        # Verify deleted
        result = await db_session.execute(select(Project).where(Project.id == p.id))
        assert result.scalar_one_or_none() is None


# ── Admin CRUD: Work History ─────────────────────────────────────────────────

class TestAdminWorkHistory:
    async def test_create_work(self, client, admin_headers):
        payload = {
            "title": "Developer",
            "company": "Tech Corp",
            "period": "2022-2024",
            "description": "Full stack developer",
            "achievements": ["Built main product"],
        }
        resp = await client.post("/api/admin/work-history", json=payload, headers=admin_headers)
        assert resp.status_code == 201
        assert resp.json()["title"] == "Developer"

    async def test_update_work(self, client, db_session, admin_headers):
        w = await insert_work(db_session)
        resp = await client.put(f"/api/admin/work-history/{w.id}", json={"company": "New Corp"}, headers=admin_headers)
        assert resp.status_code == 200
        assert resp.json()["company"] == "New Corp"

    async def test_delete_work(self, client, db_session, admin_headers):
        w = await insert_work(db_session)
        resp = await client.delete(f"/api/admin/work-history/{w.id}", headers=admin_headers)
        assert resp.status_code == 200


# ── Admin CRUD: Teaching History ─────────────────────────────────────────────

class TestAdminTeaching:
    async def test_create_teaching(self, client, admin_headers):
        payload = {
            "title": "Professor",
            "company": "University",
            "period": "2023-2024",
            "description": "Teaching web development",
            "activities": ["Created course material"],
        }
        resp = await client.post("/api/admin/teaching", json=payload, headers=admin_headers)
        assert resp.status_code == 201
        assert resp.json()["title"] == "Professor"

    async def test_update_teaching(self, client, db_session, admin_headers):
        t = await insert_teaching(db_session)
        resp = await client.put(f"/api/admin/teaching/{t.id}", json={"company": "New Uni"}, headers=admin_headers)
        assert resp.status_code == 200
        assert resp.json()["company"] == "New Uni"

    async def test_delete_teaching(self, client, db_session, admin_headers):
        t = await insert_teaching(db_session)
        resp = await client.delete(f"/api/admin/teaching/{t.id}", headers=admin_headers)
        assert resp.status_code == 200
