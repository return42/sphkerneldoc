.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/aspeed/pinctrl-aspeed.c

.. _`aspeed_sig_desc_eval`:

aspeed_sig_desc_eval
====================

.. c:function:: bool aspeed_sig_desc_eval(const struct aspeed_sig_desc *desc, bool enabled, struct regmap *map)

    :param const struct aspeed_sig_desc \*desc:
        The signal descriptor of interest

    :param bool enabled:
        True to query the enabled state, false to query disabled state

    :param struct regmap \*map:
        *undescribed*

.. _`aspeed_sig_desc_eval.description`:

Description
-----------

@return True if the descriptor's bitfield is configured to the state
selected by \ ``enabled``\ , false otherwise

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

.. c:function:: bool aspeed_sig_expr_eval(const struct aspeed_sig_expr *expr, bool enabled, struct regmap *map)

    :param const struct aspeed_sig_expr \*expr:
        An expression controlling the signal for a mux function on a pin

    :param bool enabled:
        True to query the enabled state, false to query disabled state

    :param struct regmap \*map:
        *undescribed*

.. _`aspeed_sig_expr_eval.description`:

Description
-----------

@return True if the expression composed by \ ``enabled``\  evaluates true, false
otherwise

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

.. c:function:: bool aspeed_sig_expr_set(const struct aspeed_sig_expr *expr, bool enable, struct regmap *map)

    all descriptors in the expression.

    :param const struct aspeed_sig_expr \*expr:
        The expression associated with the function whose signal is to be
        configured

    :param bool enable:
        true to enable an function's signal through a pin's signal
        expression, false to disable the function's signal

    :param struct regmap \*map:
        The SCU's regmap instance for pinmux register access.

.. _`aspeed_sig_expr_set.description`:

Description
-----------

@return true if the expression is configured as requested, false otherwise

.. _`aspeed_disable_sig`:

aspeed_disable_sig
==================

.. c:function:: bool aspeed_disable_sig(const struct aspeed_sig_expr **exprs, struct regmap *map)

    :param const struct aspeed_sig_expr \*\*exprs:
        The list of signal expressions (from a priority level on a pin)

    :param struct regmap \*map:
        The SCU's regmap instance for pinmux register access.

.. _`aspeed_disable_sig.description`:

Description
-----------

@return true if all expressions in the list are successfully disabled, false
otherwise

.. _`aspeed_find_expr_by_name`:

aspeed_find_expr_by_name
========================

.. c:function:: const struct aspeed_sig_expr *aspeed_find_expr_by_name(const struct aspeed_sig_expr **exprs, const char *name)

    requested function.

    :param const struct aspeed_sig_expr \*\*exprs:
        List of signal expressions (haystack)

    :param const char \*name:
        The name of the requested function (needle)

.. _`aspeed_find_expr_by_name.description`:

Description
-----------

@return A pointer to the signal expression whose function tag matches the
provided name, otherwise NULL.

.. This file was automatic generated / don't edit.

