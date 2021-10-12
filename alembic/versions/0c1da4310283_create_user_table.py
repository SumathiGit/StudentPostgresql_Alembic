"""create user table

Revision ID: 0c1da4310283
Revises: 
Create Date: 2021-10-12 10:26:56.094952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c1da4310283'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True,unique=True),
        sa.Column('username', sa.String(100), unique=True),
        sa.Column('hashed_password',sa.String(100)),
        sa.Column('email',sa.String(191), unique=True),
        sa.Column('is_active',sa.Boolean),
        sa.Column('created_date',sa.DateTime)
    )



def downgrade():
    pass
