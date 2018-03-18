"""empty message

Revision ID: 18c931f6ddf5
Revises: db2f05fa675f
Create Date: 2018-03-17 19:23:34.689049

"""

# revision identifiers, used by Alembic.
revision = '18c931f6ddf5'
down_revision = 'db2f05fa675f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permission',
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['resource_id'], ['resources.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('permission')
    ### end Alembic commands ###
