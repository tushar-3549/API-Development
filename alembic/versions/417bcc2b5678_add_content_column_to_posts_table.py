"""add content column to posts table

Revision ID: 417bcc2b5678
Revises: d377e229e26f
Create Date: 2024-12-21 15:36:03.804163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '417bcc2b5678'
down_revision: Union[str, None] = 'd377e229e26f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
