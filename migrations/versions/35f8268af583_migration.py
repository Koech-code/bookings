"""Migration

Revision ID: 35f8268af583
Revises: a306d9c4421a
Create Date: 2021-08-26 17:04:34.387385

"""

# revision identifiers, used by Alembic.
revision = '35f8268af583'
down_revision = 'a306d9c4421a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sessions', sa.Column('tarehe', sa.DateTime(timezone=255), nullable=True))
    op.drop_column('sessions', 'dat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sessions', sa.Column('dat', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.drop_column('sessions', 'tarehe')
    # ### end Alembic commands ###
