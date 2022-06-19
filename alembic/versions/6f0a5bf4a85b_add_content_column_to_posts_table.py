"""add content column to posts table

Revision ID: 6f0a5bf4a85b
Revises: a2e5a388cda2
Create Date: 2022-06-17 16:05:53.085692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f0a5bf4a85b'
down_revision = 'a2e5a388cda2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
