.. -*- coding: utf-8; mode: rst -*-

=======
clock.c
=======


.. _`davinci_set_pllrate`:

davinci_set_pllrate
===================

.. c:function:: int davinci_set_pllrate (struct pll_data *pll, unsigned int prediv, unsigned int mult, unsigned int postdiv)

    set the output rate of a given PLL.

    :param struct pll_data \*pll:
        pll whose rate needs to be changed.

    :param unsigned int prediv:
        The pre divider value. Passing 0 disables the pre-divider.

    :param unsigned int mult:

        *undescribed*

    :param unsigned int postdiv:
        The post divider value. Passing 0 disables the post-divider.



.. _`davinci_set_pllrate.note`:

Note
----

Currently tested to work with OMAP-L138 only.



.. _`davinci_set_refclk_rate`:

davinci_set_refclk_rate
=======================

.. c:function:: int davinci_set_refclk_rate (unsigned long rate)

    Set the reference clock rate

    :param unsigned long rate:
        The new rate.



.. _`davinci_set_refclk_rate.description`:

Description
-----------

Sets the reference clock rate to a given value. This will most likely
result in the entire clock tree getting updated.

This is used to support boards which use a reference clock different
than that used by default in <soc>.c file. The reference clock rate
should be updated early in the boot process; ideally soon after the
clock tree has been initialized once with the default reference clock
rate (:c:func:`davinci_common_init`).

Returns 0 on success, error otherwise.

