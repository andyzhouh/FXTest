"""empty message

Revision ID: 1d9f0c8771ba
Revises: 
Create Date: 2018-04-28 15:59:04.658851

"""
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '1d9f0c8771ba'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'interfacetests', 'interfacetests', ['pid'], ['id'])
def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'tstresults', type_='foreignkey')
    op.add_column('tasks', sa.Column('taskdesc', sa.TEXT(length=252), nullable=True))
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_constraint(None, 'projects', type_='unique')
    op.drop_constraint(None, 'interfacetests', type_='foreignkey')
    # ### end Alembic commands ###