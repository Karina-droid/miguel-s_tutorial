"""empty message

Revision ID: 40fbc578f4cd
Revises: 8e6aee1e3def
Create Date: 2021-02-06 14:04:49.665499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40fbc578f4cd'
down_revision = '8e6aee1e3def'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
