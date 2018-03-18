"""empty message

Revision ID: aff0e93d7b57
Revises: 9f1c68019eb8
Create Date: 2018-03-16 21:28:43.446789

"""

# revision identifiers, used by Alembic.
revision = 'aff0e93d7b57'
down_revision = '9f1c68019eb8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resources')
    op.drop_table('groups')
    ### end Alembic commands ###
