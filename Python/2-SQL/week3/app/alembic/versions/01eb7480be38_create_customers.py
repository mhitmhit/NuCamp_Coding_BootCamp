"""create customers

Revision ID: 01eb7480be38
Revises:
Create Date: 2024-06-28 14:22:41.816965

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01eb7480be38'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
