.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/reset-controller.h

.. _`reset_control_ops`:

struct reset_control_ops
========================

.. c:type:: struct reset_control_ops


.. _`reset_control_ops.definition`:

Definition
----------

.. code-block:: c

    struct reset_control_ops {
        int (* reset) (struct reset_controller_dev *rcdev, unsigned long id);
        int (* assert) (struct reset_controller_dev *rcdev, unsigned long id);
        int (* deassert) (struct reset_controller_dev *rcdev, unsigned long id);
        int (* status) (struct reset_controller_dev *rcdev, unsigned long id);
    }

.. _`reset_control_ops.members`:

Members
-------

reset
    for self-deasserting resets, does all necessary
    things to reset the device

assert
    manually assert the reset line, if supported

deassert
    manually deassert the reset line, if supported

status
    return the status of the reset line, if supported

.. _`reset_controller_dev`:

struct reset_controller_dev
===========================

.. c:type:: struct reset_controller_dev

    reset controller entity that might provide multiple reset controls

.. _`reset_controller_dev.definition`:

Definition
----------

.. code-block:: c

    struct reset_controller_dev {
        const struct reset_control_ops *ops;
        struct module *owner;
        struct list_head list;
        struct list_head reset_control_head;
        struct device_node *of_node;
        int of_reset_n_cells;
        int (* of_xlate) (struct reset_controller_dev *rcdev,const struct of_phandle_args *reset_spec);
        unsigned int nr_resets;
    }

.. _`reset_controller_dev.members`:

Members
-------

ops
    a pointer to device specific struct reset_control_ops

owner
    kernel module of the reset controller driver

list
    internal list of reset controller devices

reset_control_head
    head of internal list of requested reset controls

of_node
    corresponding device tree node as phandle target

of_reset_n_cells
    number of cells in reset line specifiers

of_xlate
    translation function to translate from specifier as found in the
    device tree to id as given to the reset control ops

nr_resets
    number of reset controls in this reset controller device

.. This file was automatic generated / don't edit.

