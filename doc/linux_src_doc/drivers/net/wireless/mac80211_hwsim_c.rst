.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/mac80211_hwsim.c

.. _`hwsim_regtest`:

enum hwsim_regtest
==================

.. c:type:: enum hwsim_regtest

    the type of regulatory tests we offer

.. _`hwsim_regtest.definition`:

Definition
----------

.. code-block:: c

    enum hwsim_regtest {
        HWSIM_REGTEST_DISABLED,
        HWSIM_REGTEST_DRIVER_REG_FOLLOW,
        HWSIM_REGTEST_DRIVER_REG_ALL,
        HWSIM_REGTEST_DIFF_COUNTRY,
        HWSIM_REGTEST_WORLD_ROAM,
        HWSIM_REGTEST_CUSTOM_WORLD,
        HWSIM_REGTEST_CUSTOM_WORLD_2,
        HWSIM_REGTEST_STRICT_FOLLOW,
        HWSIM_REGTEST_STRICT_ALL,
        HWSIM_REGTEST_STRICT_AND_DRIVER_REG,
        HWSIM_REGTEST_ALL
    };

.. _`hwsim_regtest.constants`:

Constants
---------

HWSIM_REGTEST_DISABLED
    No regulatory tests are performed,
    this is the default value.

HWSIM_REGTEST_DRIVER_REG_FOLLOW
    Used for testing the driver regulatory
    hint, only one driver regulatory hint will be sent as such the
    secondary radios are expected to follow.

HWSIM_REGTEST_DRIVER_REG_ALL
    Used for testing the driver regulatory
    request with all radios reporting the same regulatory domain.

HWSIM_REGTEST_DIFF_COUNTRY
    Used for testing the drivers calling
    different regulatory domains requests. Expected behaviour is for
    an intersection to occur but each device will still use their
    respective regulatory requested domains. Subsequent radios will
    use the resulting intersection.

HWSIM_REGTEST_WORLD_ROAM
    Used for testing the world roaming. We accomplish
    this by using a custom beacon-capable regulatory domain for the first
    radio. All other device world roam.

HWSIM_REGTEST_CUSTOM_WORLD
    Used for testing the custom world regulatory
    domain requests. All radios will adhere to this custom world regulatory
    domain.

HWSIM_REGTEST_CUSTOM_WORLD_2
    Used for testing 2 custom world regulatory
    domain requests. The first radio will adhere to the first custom world
    regulatory domain, the second one to the second custom world regulatory
    domain. All other devices will world roam.

HWSIM_REGTEST_STRICT_FOLLOW
    *undescribed*

HWSIM_REGTEST_STRICT_ALL
    Used for testing strict regulatory domain
    settings. All radios will adhere to this.

HWSIM_REGTEST_STRICT_AND_DRIVER_REG
    Used for testing strict regulatory
    domain settings, combined with secondary driver regulatory domain
    settings. The first radio will get a strict regulatory domain setting
    using the first driver regulatory request and the second radio will use
    non-strict settings using the second driver regulatory request. All
    other devices should follow the intersection created between the
    first two.

HWSIM_REGTEST_ALL
    Used for testing every possible mix. You will need
    at least 6 radios for a complete test. We will test in this order:
    1 - driver custom world regulatory domain
    2 - second custom world regulatory domain
    3 - first driver regulatory domain request
    4 - second driver regulatory domain request
    5 - strict regulatory domain settings using the third driver regulatory
    domain request
    6 and on - should follow the intersection of the 3rd, 4rth and 5th radio
    regulatory requests.

.. _`hwsim_regtest.description`:

Description
-----------

These are the different values you can use for the regtest
module parameter. This is useful to help test world roaming
and the driver \ :c:func:`regulatory_hint`\  call and combinations of these.
If you want to do specific alpha2 regulatory domain tests simply
use the userspace regulatory request as that will be respected as
well without the need of this module parameter. This is designed
only for testing the driver regulatory request, world roaming
and all possible combinations.

.. This file was automatic generated / don't edit.

