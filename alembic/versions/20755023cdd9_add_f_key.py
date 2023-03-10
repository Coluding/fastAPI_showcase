"""add f key

Revision ID: 20755023cdd9
Revises: 6111420c5909
Create Date: 2022-12-22 21:34:40.950016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20755023cdd9'
down_revision = '6111420c5909'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
