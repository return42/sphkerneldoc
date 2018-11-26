.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/aspeed/pinctrl-aspeed.h

.. _`sig_desc_bit`:

SIG_DESC_BIT
============

.. c:function::  SIG_DESC_BIT( reg,  idx,  val)

    hand macro for describing an SCU descriptor enabled by the state of one bit. The disable value is derived.

    :param reg:
        The signal's associated register, offset from base
    :type reg: 

    :param idx:
        The signal's bit index in the register
    :type idx: 

    :param val:
        The value (0 or 1) that enables the function
    :type val: 

.. _`sig_desc_set`:

SIG_DESC_SET
============

.. c:function::  SIG_DESC_SET( reg,  idx)

    hand macro expanding to an SCU descriptor enabled by a set bit.

    :param reg:
        The register, offset from base
    :type reg: 

    :param idx:
        The bit index in the register
    :type idx: 

.. _`sig_expr_decl`:

SIG_EXPR_DECL
=============

.. c:function::  SIG_EXPR_DECL( sig,  func,  ...)

    :param sig:
        A macro symbol name for the signal (is subjected to stringification
        and token pasting)
    :type sig: 

    :param func:
        The function in which the signal is participating
    :type func: 

    :param ellipsis ellipsis:
        Signal descriptors that define the signal expression

.. _`sig_expr_decl.description`:

Description
-----------

For example, the following declares the ROMD8 signal for the ROM16 function:

SIG_EXPR_DECL(ROMD8, ROM16, SIG_DESC_SET(SCU90, 6));

.. _`sig_expr_decl.and-with-multiple-signal-descriptors`:

And with multiple signal descriptors
------------------------------------


SIG_EXPR_DECL(ROMD8, ROM16S, SIG_DESC_SET(HW_STRAP1, 4),
{ HW_STRAP1, GENMASK(1, 0), 0, 0 });

.. _`sig_expr_ptr`:

SIG_EXPR_PTR
============

.. c:function::  SIG_EXPR_PTR( sig,  func)

    :param sig:
        The macro symbol name for the signal (subjected to token pasting)
    :type sig: 

    :param func:
        The macro symbol name for the function (subjected to token pasting)
    :type func: 

.. _`sig_expr_list_decl`:

SIG_EXPR_LIST_DECL
==================

.. c:function::  SIG_EXPR_LIST_DECL( sig,  ...)

    :param sig:
        A macro symbol name for the signal (is subjected to token pasting)
    :type sig: 

    :param ellipsis ellipsis:
        Signal expression structure pointers (use \ :c:func:`SIG_EXPR_PTR`\ )

.. _`sig_expr_list_decl.description`:

Description
-----------

For example, the 16-bit ROM bus can be enabled by one of two possible signal

.. _`sig_expr_list_decl.expressions`:

expressions
-----------


SIG_EXPR_DECL(ROMD8, ROM16, SIG_DESC_SET(SCU90, 6));
SIG_EXPR_DECL(ROMD8, ROM16S, SIG_DESC_SET(HW_STRAP1, 4),
{ HW_STRAP1, GENMASK(1, 0), 0, 0 });
SIG_EXPR_LIST_DECL(ROMD8, SIG_EXPR_PTR(ROMD8, ROM16),
SIG_EXPR_PTR(ROMD8, ROM16S));

.. _`sig_expr_list_decl_single`:

SIG_EXPR_LIST_DECL_SINGLE
=========================

.. c:function::  SIG_EXPR_LIST_DECL_SINGLE( sig,  func,  ...)

    hand macro for declaring a function expression and an expression list with a single function.

    :param sig:
        *undescribed*
    :type sig: 

    :param func:
        A macro symbol name for the function (is subjected to token pasting)
    :type func: 

    :param ellipsis ellipsis:
        Function descriptors that define the function expression

.. _`sig_expr_list_decl_single.description`:

Description
-----------

For example, signal NCTS6 participates in its own function with one group:

SIG_EXPR_LIST_DECL_SINGLE(NCTS6, NCTS6, SIG_DESC_SET(SCU90, 7));

.. _`ms_pin_decl`:

MS_PIN_DECL
===========

.. c:function::  MS_PIN_DECL( pin,  other,  high,  low)

    signal pin

    :param pin:
        The pin number
    :type pin: 

    :param other:
        Macro name for "other" functionality (subjected to stringification)
    :type other: 

    :param high:
        Macro name for the highest priority signal functions
    :type high: 

    :param low:
        Macro name for the low signal functions
    :type low: 

.. _`ms_pin_decl.for-example`:

For example
-----------


#define A8 56
SIG_EXPR_DECL(ROMD8, ROM16, SIG_DESC_SET(SCU90, 6));
SIG_EXPR_DECL(ROMD8, ROM16S, SIG_DESC_SET(HW_STRAP1, 4),
{ HW_STRAP1, GENMASK(1, 0), 0, 0 });
SIG_EXPR_LIST_DECL(ROMD8, SIG_EXPR_PTR(ROMD8, ROM16),
SIG_EXPR_PTR(ROMD8, ROM16S));
SIG_EXPR_LIST_DECL_SINGLE(NCTS6, NCTS6, SIG_DESC_SET(SCU90, 7));
MS_PIN_DECL(A8, GPIOH0, ROMD8, NCTS6);

.. _`ss_pin_decl`:

SS_PIN_DECL
===========

.. c:function::  SS_PIN_DECL( pin,  other,  sig)

    :param pin:
        The pin number
    :type pin: 

    :param other:
        Macro name for "other" functionality (subjected to stringification)
    :type other: 

    :param sig:
        Macro name for the signal (subjected to stringification)
    :type sig: 

.. _`ss_pin_decl.for-example`:

For example
-----------


#define E3 80
SIG_EXPR_LIST_DECL_SINGLE(SCL5, I2C5, I2C5_DESC);
SS_PIN_DECL(E3, GPIOK0, SCL5);

.. _`sssf_pin_decl`:

SSSF_PIN_DECL
=============

.. c:function::  SSSF_PIN_DECL( pin,  other,  sig,  ...)

    :param pin:
        The pin number
    :type pin: 

    :param other:
        Macro name for "other" functionality (subjected to stringification)
    :type other: 

    :param sig:
        Macro name for the signal (subjected to stringification)
    :type sig: 

    :param ellipsis ellipsis:
        Signal descriptors that define the function expression

.. _`sssf_pin_decl.for-example`:

For example
-----------


SSSF_PIN_DECL(A4, GPIOA2, TIMER3, SIG_DESC_SET(SCU80, 2));

.. This file was automatic generated / don't edit.

