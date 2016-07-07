.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/completion.h

.. _`declare_completion`:

DECLARE_COMPLETION
==================

.. c:function::  DECLARE_COMPLETION( work)

    declare and initialize a completion structure

    :param  work:
        identifier for the completion structure

.. _`declare_completion.description`:

Description
-----------

This macro declares and initializes a completion structure. Generally used
for static declarations. You should use the \_ONSTACK variant for automatic
variables.

.. _`declare_completion_onstack`:

DECLARE_COMPLETION_ONSTACK
==========================

.. c:function::  DECLARE_COMPLETION_ONSTACK( work)

    declare and initialize a completion structure

    :param  work:
        identifier for the completion structure

.. _`declare_completion_onstack.description`:

Description
-----------

This macro declares and initializes a completion structure on the kernel
stack.

.. _`init_completion`:

init_completion
===============

.. c:function:: void init_completion(struct completion *x)

    Initialize a dynamically allocated completion

    :param struct completion \*x:
        pointer to completion structure that is to be initialized

.. _`init_completion.description`:

Description
-----------

This inline function will initialize a dynamically created completion
structure.

.. _`reinit_completion`:

reinit_completion
=================

.. c:function:: void reinit_completion(struct completion *x)

    reinitialize a completion structure

    :param struct completion \*x:
        pointer to completion structure that is to be reinitialized

.. _`reinit_completion.description`:

Description
-----------

This inline function should be used to reinitialize a completion structure so it can
be reused. This is especially important after \ :c:func:`complete_all`\  is used.

.. This file was automatic generated / don't edit.

