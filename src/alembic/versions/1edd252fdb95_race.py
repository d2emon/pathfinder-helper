"""Race

Revision ID: 1edd252fdb95
Revises: 9f7e63f7d0eb
Create Date: 2017-03-12 16:34:29.025133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1edd252fdb95'
down_revision = '9f7e63f7d0eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('race',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('custom_ability', sa.Integer(), nullable=True),
    sa.Column('bonus_feat', sa.Integer(), nullable=True),
    sa.Column('bonus_skill', sa.Integer(), nullable=True),
    sa.Column('size_bonus', sa.Integer(), nullable=True),
    sa.Column('speed', sa.Integer(), nullable=True),
    sa.Column('description', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('race')
    # ### end Alembic commands ###
