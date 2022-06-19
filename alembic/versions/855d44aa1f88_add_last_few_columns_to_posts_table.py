"""add last few columns to posts table

Revision ID: 855d44aa1f88
Revises: d23bad5a7811
Create Date: 2022-06-18 16:24:01.174007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '855d44aa1f88'
down_revision = 'd23bad5a7811'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
