.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fpga/fpga-mgr.h

.. _`fpga_mgr_states`:

enum fpga_mgr_states
====================

.. c:type:: enum fpga_mgr_states

    fpga framework states

.. _`fpga_mgr_states.definition`:

Definition
----------

.. code-block:: c

    enum fpga_mgr_states {
        FPGA_MGR_STATE_UNKNOWN,
        FPGA_MGR_STATE_POWER_OFF,
        FPGA_MGR_STATE_POWER_UP,
        FPGA_MGR_STATE_RESET,
        FPGA_MGR_STATE_FIRMWARE_REQ,
        FPGA_MGR_STATE_FIRMWARE_REQ_ERR,
        FPGA_MGR_STATE_WRITE_INIT,
        FPGA_MGR_STATE_WRITE_INIT_ERR,
        FPGA_MGR_STATE_WRITE,
        FPGA_MGR_STATE_WRITE_ERR,
        FPGA_MGR_STATE_WRITE_COMPLETE,
        FPGA_MGR_STATE_WRITE_COMPLETE_ERR,
        FPGA_MGR_STATE_OPERATING
    };

.. _`fpga_mgr_states.constants`:

Constants
---------

FPGA_MGR_STATE_UNKNOWN
    can't determine state

FPGA_MGR_STATE_POWER_OFF
    FPGA power is off

FPGA_MGR_STATE_POWER_UP
    FPGA reports power is up

FPGA_MGR_STATE_RESET
    FPGA in reset state

FPGA_MGR_STATE_FIRMWARE_REQ
    firmware request in progress

FPGA_MGR_STATE_FIRMWARE_REQ_ERR
    firmware request failed

FPGA_MGR_STATE_WRITE_INIT
    preparing FPGA for programming

FPGA_MGR_STATE_WRITE_INIT_ERR
    Error during WRITE_INIT stage

FPGA_MGR_STATE_WRITE
    writing image to FPGA

FPGA_MGR_STATE_WRITE_ERR
    Error while writing FPGA

FPGA_MGR_STATE_WRITE_COMPLETE
    Doing post programming steps

FPGA_MGR_STATE_WRITE_COMPLETE_ERR
    Error during WRITE_COMPLETE

FPGA_MGR_STATE_OPERATING
    FPGA is programmed and operating

.. _`fpga_manager_ops`:

struct fpga_manager_ops
=======================

.. c:type:: struct fpga_manager_ops

    ops for low level fpga manager drivers

.. _`fpga_manager_ops.definition`:

Definition
----------

.. code-block:: c

    struct fpga_manager_ops {
        enum fpga_mgr_states (* state) (struct fpga_manager *mgr);
        int (* write_init) (struct fpga_manager *mgr, u32 flags,const char *buf, size_t count);
        int (* write) (struct fpga_manager *mgr, const char *buf, size_t count);
        int (* write_complete) (struct fpga_manager *mgr, u32 flags);
        void (* fpga_remove) (struct fpga_manager *mgr);
    }

.. _`fpga_manager_ops.members`:

Members
-------

state
    returns an enum value of the FPGA's state

write_init
    prepare the FPGA to receive confuration data

write
    write count bytes of configuration data to the FPGA

write_complete
    set FPGA to operating state after writing is done

fpga_remove
    optional: Set FPGA into a specific state during driver remove

.. _`fpga_manager_ops.description`:

Description
-----------

fpga_manager_ops are the low level functions implemented by a specific
fpga manager driver.  The optional ones are tested for NULL before being
called, so leaving them out is fine.

.. _`fpga_manager`:

struct fpga_manager
===================

.. c:type:: struct fpga_manager

    fpga manager structure

.. _`fpga_manager.definition`:

Definition
----------

.. code-block:: c

    struct fpga_manager {
        const char *name;
        struct device dev;
        struct mutex ref_mutex;
        enum fpga_mgr_states state;
        const struct fpga_manager_ops *mops;
        void *priv;
    }

.. _`fpga_manager.members`:

Members
-------

name
    name of low level fpga manager

dev
    fpga manager device

ref_mutex
    only allows one reference to fpga manager

state
    state of fpga manager

mops
    pointer to struct of fpga manager ops

priv
    low level driver private date

.. This file was automatic generated / don't edit.

