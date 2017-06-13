.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinmux.h

.. _`function_desc`:

struct function_desc
====================

.. c:type:: struct function_desc

    generic function descriptor

.. _`function_desc.definition`:

Definition
----------

.. code-block:: c

    struct function_desc {
        const char *name;
        const char **group_names;
        int num_group_names;
        void *data;
    }

.. _`function_desc.members`:

Members
-------

name
    name of the function

group_names
    array of pin group names

num_group_names
    number of pin group names

data
    pin controller driver specific data

.. This file was automatic generated / don't edit.

