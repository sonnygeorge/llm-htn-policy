from src.dm_env import run_dungeon_master_htn_policy_simulation
from src.utils import get_pretty_htn_string
from tests.test_utils import (
    MOCK_HTN_POLICY_FOR_PRETTY_HTN_STRING,
    test_get_pretty_htn_string,
)

test_get_pretty_htn_string()
print(get_pretty_htn_string(MOCK_HTN_POLICY_FOR_PRETTY_HTN_STRING))

# Not yet implemented (soon)
# run_dungeon_master_htn_policy_simulation()
