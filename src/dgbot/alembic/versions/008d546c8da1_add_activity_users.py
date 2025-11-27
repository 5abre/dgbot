"""add_activity_users

Revision ID: 008d546c8da1
Revises: 2bdfe8437141
Create Date: 2025-11-27 23:24:37.322397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '008d546c8da1'
down_revision: Union[str, Sequence[str], None] = '2bdfe8437141'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('last_activity', sa.Date(), nullable=True))
    op.add_column('users', sa.Column('consecutive_days', sa.Integer(), nullable=True, server_default='0'))

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'last_activity')
    op.drop_column('users', 'consecutive_days')