"""empty message

Revision ID: 00ae97767186
Revises: aff0e93d7b57
Create Date: 2018-03-17 19:14:52.765383

"""

# revision identifiers, used by Alembic.
revision = '00ae97767186'
down_revision = 'aff0e93d7b57'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_group',
    sa.Column('user_id', sa.String(length=24), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], )
    )
    op.drop_table('resources')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resources',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_group')
    ### end Alembic commands ###