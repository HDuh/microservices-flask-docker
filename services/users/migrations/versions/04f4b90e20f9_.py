"""empty message

Revision ID: 04f4b90e20f9
Revises: 2ad175ef35e5
Create Date: 2022-10-07 13:51:43.467458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04f4b90e20f9'
down_revision = '2ad175ef35e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['username'])
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###