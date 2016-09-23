.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/ts72xx_wdt.c

.. _`ts72xx_wdt`:

struct ts72xx_wdt
=================

.. c:type:: struct ts72xx_wdt

    watchdog control structure

.. _`ts72xx_wdt.definition`:

Definition
----------

.. code-block:: c

    struct ts72xx_wdt {
        struct mutex lock;
        int regval;
    #define TS72XX_WDT_BUSY_FLAG 1
    #define TS72XX_WDT_EXPECT_CLOSE_FLAG 2
        int flags;
        void __iomem *control_reg;
        void __iomem *feed_reg;
        struct platform_device *pdev;
    }

.. _`ts72xx_wdt.members`:

Members
-------

lock
    lock that protects this structure

regval
    watchdog timeout value suitable for control register

flags
    flags controlling watchdog device state

control_reg
    watchdog control register

feed_reg
    watchdog feed register

pdev
    back pointer to platform dev

.. _`timeout_to_regval`:

timeout_to_regval
=================

.. c:function:: int timeout_to_regval(int new_timeout)

    converts given timeout to control register value

    :param int new_timeout:
        timeout in seconds to be converted

.. _`timeout_to_regval.description`:

Description
-----------

Function converts given \ ``new_timeout``\  into valid value that can
be programmed into watchdog control register. When conversion is
not possible, function returns \ ``-EINVAL``\ .

.. _`regval_to_timeout`:

regval_to_timeout
=================

.. c:function:: int regval_to_timeout(int regval)

    converts control register value to timeout

    :param int regval:
        control register value to be converted

.. _`regval_to_timeout.description`:

Description
-----------

Function converts given \ ``regval``\  to timeout in seconds (1, 2, 4 or 8).
If \ ``regval``\  cannot be converted, function returns \ ``-EINVAL``\ .

.. _`ts72xx_wdt_kick`:

ts72xx_wdt_kick
===============

.. c:function:: void ts72xx_wdt_kick(struct ts72xx_wdt *wdt)

    kick the watchdog

    :param struct ts72xx_wdt \*wdt:
        watchdog to be kicked

.. _`ts72xx_wdt_kick.description`:

Description
-----------

Called with \ ``wdt``\ ->lock held.

.. _`ts72xx_wdt_start`:

ts72xx_wdt_start
================

.. c:function:: void ts72xx_wdt_start(struct ts72xx_wdt *wdt)

    starts the watchdog timer

    :param struct ts72xx_wdt \*wdt:
        watchdog to be started

.. _`ts72xx_wdt_start.description`:

Description
-----------

This function programs timeout to watchdog timer
and starts it.

Called with \ ``wdt``\ ->lock held.

.. _`ts72xx_wdt_stop`:

ts72xx_wdt_stop
===============

.. c:function:: void ts72xx_wdt_stop(struct ts72xx_wdt *wdt)

    stops the watchdog timer

    :param struct ts72xx_wdt \*wdt:
        watchdog to be stopped

.. _`ts72xx_wdt_stop.description`:

Description
-----------

Called with \ ``wdt``\ ->lock held.

.. This file was automatic generated / don't edit.

