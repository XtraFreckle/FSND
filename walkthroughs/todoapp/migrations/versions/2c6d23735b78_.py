"""empty message

Revision ID: 2c6d23735b78
Revises: dcebcd2fbcf9
Create Date: 2020-06-10 09:23:29.473684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c6d23735b78'
down_revision = 'dcebcd2fbcf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todolists', sa.Column('completed', sa.Boolean(), nullable=True))
    op.execute('UPDATE todolists SET completed = False WHERE completed IS NULL')
    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todolists', 'completed')
    # ### end Alembic commands ###
