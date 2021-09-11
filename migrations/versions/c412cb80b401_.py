"""empty message

Revision ID: c412cb80b401
Revises: 8369118943a1
Create Date: 2021-09-11 04:21:43.072350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c412cb80b401'
down_revision = '8369118943a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'challenges', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'challenges', type_='foreignkey')
    # ### end Alembic commands ###
