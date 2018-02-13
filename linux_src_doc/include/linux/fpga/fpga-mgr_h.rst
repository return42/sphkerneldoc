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

.. _`fpga_image_info`:

struct fpga_image_info
======================

.. c:type:: struct fpga_image_info

    information specific to a FPGA image

.. _`fpga_image_info.definition`:

Definition
----------

.. code-block:: c

    struct fpga_image_info {
        u32 flags;
        u32 enable_timeout_us;
        u32 disable_timeout_us;
        u32 config_complete_timeout_us;
        char *firmware_name;
        struct sg_table *sgt;
        const char *buf;
        size_t count;
        struct device *dev;
    #ifdef CONFIG_OF
        struct device_node *overlay;
    #endif
    }

.. _`fpga_image_info.members`:

Members
-------

flags
    boolean flags as defined above

enable_timeout_us
    maximum time to enable traffic through bridge (uSec)

disable_timeout_us
    maximum time to disable traffic through bridge (uSec)

config_complete_timeout_us
    maximum time for FPGA to switch to operating
    status in the write_complete op.

firmware_name
    name of FPGA image firmware file

sgt
    scatter/gather table containing FPGA image

buf
    contiguous buffer containing FPGA image

count
    size of buf

dev
    device that owns this

overlay
    Device Tree overlay

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
        size_t initial_header_size;
        enum fpga_mgr_states (*state)(struct fpga_manager *mgr);
        int (*write_init)(struct fpga_manager *mgr,struct fpga_image_info *info, const char *buf, size_t count);
        int (*write)(struct fpga_manager *mgr, const char *buf, size_t count);
        int (*write_sg)(struct fpga_manager *mgr, struct sg_table *sgt);
        int (*write_complete)(struct fpga_manager *mgr, struct fpga_image_info *info);
        void (*fpga_remove)(struct fpga_manager *mgr);
        const struct attribute_group **groups;
    }

.. _`fpga_manager_ops.members`:

Members
-------

initial_header_size
    Maximum number of bytes that should be passed into write_init

state
    returns an enum value of the FPGA's state

write_init
    prepare the FPGA to receive confuration data

write
    write count bytes of configuration data to the FPGA

write_sg
    write the scatter list of configuration data to the FPGA

write_complete
    set FPGA to operating state after writing is done

fpga_remove
    optional: Set FPGA into a specific state during driver remove

groups
    optional attribute groups.

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

