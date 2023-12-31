"""init

Revision ID: 5378cdc164a8
Revises: 
Create Date: 2024-01-05 14:35:59.739361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5378cdc164a8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('session_file_path', sa.String(), nullable=False),
    sa.Column('target_chat', sa.String(), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('prompt', sa.String(), nullable=True),
    sa.Column('advertising_channels', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accounts')
    # ### end Alembic commands ###
