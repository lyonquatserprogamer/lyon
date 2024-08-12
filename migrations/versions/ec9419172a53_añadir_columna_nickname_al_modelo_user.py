"""Añadir columna nickname al modelo User

Revision ID: ec9419172a53
Revises: 
Create Date: 2024-08-04 14:37:22.407181

"""
from alembic import op
import sqlalchemy as sa

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ec9419172a53'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nickname', sa.String(length=50), nullable=True))

def downgrade() -> None:
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('nickname')
