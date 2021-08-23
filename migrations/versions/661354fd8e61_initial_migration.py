"""Initial Migration

Revision ID: 661354fd8e61
Revises: None
Create Date: 2021-08-23 17:24:47.776980

"""

# revision identifiers, used by Alembic.
revision = '661354fd8e61'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('favourite_team', sa.String(length=50), nullable=True))
    op.create_index(op.f('ix_users_favourite_team'), 'users', ['favourite_team'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_favourite_team'), table_name='users')
    op.drop_column('users', 'favourite_team')
    # ### end Alembic commands ###