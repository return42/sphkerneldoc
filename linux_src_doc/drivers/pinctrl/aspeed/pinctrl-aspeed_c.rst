.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/aspeed/pinctrl-aspeed.c

.. _`aspeed_sig_desc_eval`:

aspeed_sig_desc_eval
====================

.. c:function:: int aspeed_sig_desc_eval(const struct aspeed_sig_desc *desc, bool enabled, struct regmap *map)

    :param const struct aspeed_sig_desc \*desc:
        The signal descriptor of interest

    :param bool enabled:
        True to query the enabled state, false to query disabled state

    :param struct regmap \*map:
        *undescribed*

.. _`aspeed_sig_desc_eval.return`:

Return
------

1 if the descriptor's bitfield is configured to the state
selected by \ ``enabled``\ , 0 if not, and less than zero if an unrecoverable
failure occurred

Evaluation of descriptor state is non-trivial in that it is not a binary

.. _`aspeed_sig_desc_eval.outcome`:

outcome
-------

The bitfields can be greater than one bit in size and thus can take
a value that is neither the enabled nor disabled state recorded in the
descriptor (typically this means a different function to the one of interest
is enabled). Thus we must explicitly test for either condition as required.

.. _`aspeed_sig_expr_eval`:

aspeed_sig_expr_eval
====================

.. c:function:: int aspeed_sig_expr_eval(const struct aspeed_sig_expr *expr, bool enabled, struct regmap * const *maps)

    :param const struct aspeed_sig_expr \*expr:
        An expression controlling the signal for a mux function on a pin

    :param bool enabled:
        True to query the enabled state, false to query disabled state

    :param struct regmap \* const \*maps:
        The list of regmap instances

.. _`aspeed_sig_expr_eval.return`:

Return
------

1 if the expression composed by \ ``enabled``\  evaluates true, 0 if not,
and less than zero if an unrecoverable failure occurred.

A mux function is enabled or disabled if the function's signal expression
for each pin in the function's pin group evaluates true for the desired
state. An signal expression evaluates true if all of its associated signal
descriptors evaluate true for the desired state.

If an expression's state is described by more than one bit, either through
multi-bit bitfields in a single signal descriptor or through multiple signal
descriptors of a single bit then it is possible for the expression to be in
neither the enabled nor disabled state. Thus we must explicitly test for
either condition as required.

.. _`aspeed_sig_expr_set`:

aspeed_sig_expr_set
===================

.. c:function:: int aspeed_sig_expr_set(const struct aspeed_sig_expr *expr, bool enable, struct regmap * const *maps)

    all descriptors in the expression.

    :param const struct aspeed_sig_expr \*expr:
        The expression associated with the function whose signal is to be
        configured

    :param bool enable:
        true to enable an function's signal through a pin's signal
        expression, false to disable the function's signal

    :param struct regmap \* const \*maps:
        The list of regmap instances for pinmux register access.

.. _`aspeed_sig_expr_set.return`:

Return
------

0 if the expression is configured as requested and a negative error
code otherwise

.. _`aspeed_disable_sig`:

aspeed_disable_sig
==================

.. c:function:: int aspeed_disable_sig(const struct aspeed_sig_expr **exprs, struct regmap * const *maps)

    :param const struct aspeed_sig_expr \*\*exprs:
        The list of signal expressions (from a priority level on a pin)

    :param struct regmap \* const \*maps:
        The list of regmap instances for pinmux register access.

.. _`aspeed_disable_sig.return`:

Return
------

0 if all expressions are disabled, otherwise a negative error code

.. _`aspeed_find_expr_by_name`:

aspeed_find_expr_by_name
========================

.. c:function:: const struct aspeed_sig_expr *aspeed_find_expr_by_name(const struct aspeed_sig_expr **exprs, const char *name)

    requested function.

    :param const struct aspeed_sig_expr \*\*exprs:
        List of signal expressions (haystack)

    :param const char \*name:
        The name of the requested function (needle)

.. _`aspeed_find_expr_by_name.return`:

Return
------

A pointer to the signal expression whose function tag matches the
provided name, otherwise NULL.

.. This file was automatic generated / don't edit.

