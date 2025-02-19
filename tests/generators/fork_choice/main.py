from eth2spec.gen_helpers.gen_from_tests.gen import run_state_test_generators
from eth2spec.test.helpers.constants import PHASE0, ALTAIR, MERGE


if __name__ == "__main__":
    phase_0_mods = {key: 'eth2spec.test.phase0.fork_choice.test_' + key for key in [
        'get_head',
        'on_block',
    ]}
    # No additional Altair specific finality tests, yet.
    altair_mods = phase_0_mods
    # No specific Merge tests yet.
    merge_mods = altair_mods

    all_mods = {
        PHASE0: phase_0_mods,
        ALTAIR: altair_mods,
        MERGE: merge_mods,
    }

    run_state_test_generators(runner_name="fork_choice", all_mods=all_mods)
