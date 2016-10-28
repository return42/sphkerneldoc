.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/otg-fsm.h

.. _`otg_fsm`:

struct otg_fsm
==============

.. c:type:: struct otg_fsm

    OTG state machine according to the OTG spec

.. _`otg_fsm.definition`:

Definition
----------

.. code-block:: c

    struct otg_fsm {
        int id;
        int adp_change;
        int power_up;
        int a_srp_det;
        int a_vbus_vld;
        int b_conn;
        int a_bus_resume;
        int a_bus_suspend;
        int a_conn;
        int b_se0_srp;
        int b_ssend_srp;
        int b_sess_vld;
        int test_device;
        int a_bus_drop;
        int a_bus_req;
        int b_bus_req;
        int a_sess_vld;
        int b_bus_resume;
        int b_bus_suspend;
        int drv_vbus;
        int loc_conn;
        int loc_sof;
        int adp_prb;
        int adp_sns;
        int data_pulse;
        int a_set_b_hnp_en;
        int b_srp_done;
        int b_hnp_enable;
        int a_clr_err;
        int a_bus_drop_inf;
        int a_bus_req_inf;
        int a_clr_err_inf;
        int b_bus_req_inf;
        int a_suspend_req_inf;
        int a_wait_vrise_tmout;
        int a_wait_vfall_tmout;
        int a_wait_bcon_tmout;
        int a_aidl_bdis_tmout;
        int b_ase0_brst_tmout;
        int a_bidl_adis_tmout;
        struct otg_fsm_ops *ops;
        struct usb_otg *otg;
        int protocol;
        struct mutex lock;
        u8 *host_req_flag;
        struct delayed_work hnp_polling_work;
        bool state_changed;
    }

.. _`otg_fsm.members`:

Members
-------

id
    TRUE for B-device, FALSE for A-device.

adp_change
    TRUE when current ADP measurement (n) value, compared to the
    ADP measurement taken at n-2, differs by more than CADP_THR

power_up
    TRUE when the OTG device first powers up its USB system and
    ADP measurement taken if ADP capable

a_srp_det
    TRUE if the A-device detects SRP

a_vbus_vld
    TRUE when VBUS voltage is in regulation

b_conn
    TRUE if the A-device detects connection from the B-device

a_bus_resume
    TRUE when the B-device detects that the A-device is signaling
    a resume (K state)
    B-Device state inputs

a_bus_suspend
    TRUE when the B-device detects that the A-device has put the
    bus into suspend

a_conn
    TRUE if the B-device detects a connection from the A-device

b_se0_srp
    TRUE when the line has been at SE0 for more than the minimum
    time before generating SRP

b_ssend_srp
    TRUE when the VBUS has been below VOTG_SESS_VLD for more than
    the minimum time before generating SRP

b_sess_vld
    TRUE when the B-device detects that the voltage on VBUS is
    above VOTG_SESS_VLD

test_device
    TRUE when the B-device switches to B-Host and detects an OTG
    test device. This must be set by host/hub driver

a_bus_drop
    TRUE when A-device application needs to power down the bus

a_bus_req
    TRUE when A-device application wants to use the bus.
    FALSE to suspend the bus

b_bus_req
    TRUE during the time that the Application running on the
    B-device wants to use the bus

a_sess_vld
    TRUE if the A-device detects that VBUS is above VA_SESS_VLD

b_bus_resume
    TRUE when the A-device detects that the B-device is signaling
    resume on the bus

b_bus_suspend
    TRUE when the A-device detects that the B-device has put
    the bus into suspend

drv_vbus
    TRUE when A-device is driving VBUS

loc_conn
    TRUE when the local device has signaled that it is connected
    to the bus

loc_sof
    TRUE when the local device is generating activity on the bus

adp_prb
    TRUE when the local device is in the process of doing
    ADP probing

adp_sns
    TRUE when the B-device is in the process of carrying out
    ADP sensing

data_pulse
    TRUE when the B-device is performing data line pulsing

a_set_b_hnp_en
    *undescribed*

b_srp_done
    *undescribed*

b_hnp_enable
    *undescribed*

a_clr_err
    *undescribed*

a_bus_drop_inf
    *undescribed*

a_bus_req_inf
    *undescribed*

a_clr_err_inf
    *undescribed*

b_bus_req_inf
    *undescribed*

a_suspend_req_inf
    *undescribed*

a_wait_vrise_tmout
    *undescribed*

a_wait_vfall_tmout
    *undescribed*

a_wait_bcon_tmout
    *undescribed*

a_aidl_bdis_tmout
    *undescribed*

b_ase0_brst_tmout
    *undescribed*

a_bidl_adis_tmout
    *undescribed*

ops
    *undescribed*

otg
    *undescribed*

protocol
    *undescribed*

lock
    *undescribed*

host_req_flag
    *undescribed*

hnp_polling_work
    *undescribed*

state_changed
    *undescribed*

.. _`otg_fsm.description`:

Description
-----------

OTG hardware Inputs

Common inputs for A and B device

A-Device state inputs

Application inputs (A-Device)

Application inputs (B-Device)

Auxilary inputs (OTG v1.3 only. Obsolete now.)

OTG Output status. Read only for users. Updated by OTG FSM helpers defined
in this file

Outputs for Both A and B device

Outputs for B-device state

Internal Variables

.. _`otg_fsm.a_set_b_hnp_en`:

a_set_b_hnp_en
--------------

TRUE when the A-device has successfully set the
b_hnp_enable bit in the B-device.
Unused as OTG fsm uses otg->host->b_hnp_enable instead

.. _`otg_fsm.b_srp_done`:

b_srp_done
----------

TRUE when the B-device has completed initiating SRP

.. _`otg_fsm.b_hnp_enable`:

b_hnp_enable
------------

TRUE when the B-device has accepted the
SetFeature(b_hnp_enable) B-device.
Unused as OTG fsm uses otg->gadget->b_hnp_enable instead

.. _`otg_fsm.a_clr_err`:

a_clr_err
---------

Asserted (by application ?) to clear a_vbus_err due to an
overcurrent condition and causes the A-device to transition
to a_wait_vfall

.. This file was automatic generated / don't edit.

