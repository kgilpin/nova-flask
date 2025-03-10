"""Create Garrison table

Revision ID: 68464af41206
Revises: 7641e7407c48
Create Date: 2024-08-01 18:05:48.936277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68464af41206'
down_revision: Union[str, None] = '7641e7407c48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('garrison',
    sa.Column('garrisonId', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gameId', sa.Integer(), nullable=False),
    sa.Column('starId', sa.Integer(), nullable=False),
    sa.Column('numShips', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gameId'], ['game.gameId'], ),
    sa.ForeignKeyConstraint(['starId'], ['star.starId'], ),
    sa.PrimaryKeyConstraint('garrisonId')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('garrison')
    # ### end Alembic commands ###
