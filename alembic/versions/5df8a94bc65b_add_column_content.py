"""add column content

Revision ID: 5df8a94bc65b
Revises: b43777c6b964
Create Date: 2022-12-22 21:28:05.579168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5df8a94bc65b'
down_revision = 'b43777c6b964'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
