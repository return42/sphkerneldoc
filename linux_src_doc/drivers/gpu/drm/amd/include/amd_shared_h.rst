.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/include/amd_shared.h

.. _`amd_ip_funcs`:

struct amd_ip_funcs
===================

.. c:type:: struct amd_ip_funcs

    general hooks for managing amdgpu IP Blocks

.. _`amd_ip_funcs.definition`:

Definition
----------

.. code-block:: c

    struct amd_ip_funcs {
        char *name;
        int (*early_init)(void *handle);
        int (*late_init)(void *handle);
        int (*sw_init)(void *handle);
        int (*sw_fini)(void *handle);
        int (*hw_init)(void *handle);
        int (*hw_fini)(void *handle);
        void (*late_fini)(void *handle);
        int (*suspend)(void *handle);
        int (*resume)(void *handle);
        bool (*is_idle)(void *handle);
        int (*wait_for_idle)(void *handle);
        bool (*check_soft_reset)(void *handle);
        int (*pre_soft_reset)(void *handle);
        int (*soft_reset)(void *handle);
        int (*post_soft_reset)(void *handle);
        int (*set_clockgating_state)(void *handle, enum amd_clockgating_state state);
        int (*set_powergating_state)(void *handle, enum amd_powergating_state state);
        void (*get_clockgating_state)(void *handle, u32 *flags);
    }

.. _`amd_ip_funcs.members`:

Members
-------

name
    Name of IP block

early_init

    sets up early driver state (pre sw_init),
    does not configure hw - Optional

late_init
    sets up late driver/hw state (post hw_init) - Optional

sw_init
    sets up driver state, does not configure hw

sw_fini
    tears down driver state, does not configure hw

hw_init
    sets up the hw state

hw_fini
    tears down the hw state

late_fini
    final cleanup

suspend
    handles IP specific hw/sw changes for suspend

resume
    handles IP specific hw/sw changes for resume

is_idle
    returns current IP block idle status

wait_for_idle
    poll for idle

check_soft_reset
    check soft reset the IP block

pre_soft_reset
    pre soft reset the IP block

soft_reset
    soft reset the IP block

post_soft_reset
    post soft reset the IP block

set_clockgating_state
    enable/disable cg for the IP block

set_powergating_state
    enable/disable pg for the IP block

get_clockgating_state
    get current clockgating status

.. This file was automatic generated / don't edit.

