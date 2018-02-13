.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/b43/phy_common.h

.. _`b43_interference_mitigation`:

enum b43_interference_mitigation
================================

.. c:type:: enum b43_interference_mitigation

    Interference Mitigation mode

.. _`b43_interference_mitigation.definition`:

Definition
----------

.. code-block:: c

    enum b43_interference_mitigation {
        B43_INTERFMODE_NONE,
        B43_INTERFMODE_NONWLAN,
        B43_INTERFMODE_MANUALWLAN,
        B43_INTERFMODE_AUTOWLAN
    };

.. _`b43_interference_mitigation.constants`:

Constants
---------

B43_INTERFMODE_NONE
    Disabled

B43_INTERFMODE_NONWLAN
    Non-WLAN Interference Mitigation

B43_INTERFMODE_MANUALWLAN
    WLAN Interference Mitigation

B43_INTERFMODE_AUTOWLAN
    Automatic WLAN Interference Mitigation

.. _`b43_txpwr_result`:

enum b43_txpwr_result
=====================

.. c:type:: enum b43_txpwr_result

    Return value for the recalc_txpower PHY op.

.. _`b43_txpwr_result.definition`:

Definition
----------

.. code-block:: c

    enum b43_txpwr_result {
        B43_TXPWR_RES_NEED_ADJUST,
        B43_TXPWR_RES_DONE
    };

.. _`b43_txpwr_result.constants`:

Constants
---------

B43_TXPWR_RES_NEED_ADJUST
    Values changed. Hardware adjustment is needed.

B43_TXPWR_RES_DONE
    No more work to do. Everything is done.

.. _`b43_phy_operations`:

struct b43_phy_operations
=========================

.. c:type:: struct b43_phy_operations

    Function pointers for PHY ops.

.. _`b43_phy_operations.definition`:

Definition
----------

.. code-block:: c

    struct b43_phy_operations {
        int (*allocate)(struct b43_wldev *dev);
        void (*free)(struct b43_wldev *dev);
        void (*prepare_structs)(struct b43_wldev *dev);
        int (*prepare_hardware)(struct b43_wldev *dev);
        int (*init)(struct b43_wldev *dev);
        void (*exit)(struct b43_wldev *dev);
        u16 (*phy_read)(struct b43_wldev *dev, u16 reg);
        void (*phy_write)(struct b43_wldev *dev, u16 reg, u16 value);
        void (*phy_maskset)(struct b43_wldev *dev, u16 reg, u16 mask, u16 set);
        u16 (*radio_read)(struct b43_wldev *dev, u16 reg);
        void (*radio_write)(struct b43_wldev *dev, u16 reg, u16 value);
        bool (*supports_hwpctl)(struct b43_wldev *dev);
        void (*software_rfkill)(struct b43_wldev *dev, bool blocked);
        void (*switch_analog)(struct b43_wldev *dev, bool on);
        int (*switch_channel)(struct b43_wldev *dev, unsigned int new_channel);
        unsigned int (*get_default_chan)(struct b43_wldev *dev);
        void (*set_rx_antenna)(struct b43_wldev *dev, int antenna);
        int (*interf_mitigation)(struct b43_wldev *dev, enum b43_interference_mitigation new_mode);
        enum b43_txpwr_result (*recalc_txpower)(struct b43_wldev *dev, bool ignore_tssi);
        void (*adjust_txpower)(struct b43_wldev *dev);
        void (*pwork_15sec)(struct b43_wldev *dev);
        void (*pwork_60sec)(struct b43_wldev *dev);
    }

.. _`b43_phy_operations.members`:

Members
-------

allocate
    Allocate and initialise the PHY data structures.
    Must not be NULL.

free
    Destroy and free the PHY data structures.
    Must not be NULL.

prepare_structs
    Prepare the PHY data structures.
    The data structures allocated in \ ``allocate``\  are
    initialized here.
    Must not be NULL.

prepare_hardware
    Prepare the PHY. This is called before b43_chip_init to
    do some early early PHY hardware init.
    Can be NULL, if not required.

init
    Initialize the PHY.
    Must not be NULL.

exit
    Shutdown the PHY.
    Can be NULL, if not required.

phy_read
    Read from a PHY register.
    Must not be NULL.

phy_write
    Write to a PHY register.
    Must not be NULL.

phy_maskset
    Maskset a PHY register, taking shortcuts.
    If it is NULL, a generic algorithm is used.

radio_read
    Read from a Radio register.
    Must not be NULL.

radio_write
    Write to a Radio register.
    Must not be NULL.

supports_hwpctl
    Returns a boolean whether Hardware Power Control
    is supported or not.
    If NULL, hwpctl is assumed to be never supported.

software_rfkill
    Turn the radio ON or OFF.
    Possible state values are
    RFKILL_STATE_SOFT_BLOCKED or
    RFKILL_STATE_UNBLOCKED
    Must not be NULL.

switch_analog
    Turn the Analog on/off.
    Must not be NULL.

switch_channel
    Switch the radio to another channel.
    Must not be NULL.

get_default_chan
    Just returns the default channel number.
    Must not be NULL.

set_rx_antenna
    Set the antenna used for RX.
    Can be NULL, if not supported.

interf_mitigation
    Switch the Interference Mitigation mode.
    Can be NULL, if not supported.

recalc_txpower
    Recalculate the transmission power parameters.
    This callback has to recalculate the TX power settings,
    but does not need to write them to the hardware, yet.
    Returns enum b43_txpwr_result to indicate whether the hardware
    needs to be adjusted.
    If B43_TXPWR_NEED_ADJUST is returned, \ ``adjust_txpower``\ 
    will be called later.
    If the parameter "ignore_tssi" is true, the TSSI values should
    be ignored and a recalculation of the power settings should be
    done even if the TSSI values did not change.
    This function may sleep, but should not.
    Must not be NULL.

adjust_txpower
    Write the previously calculated TX power settings
    (from \ ``recalc_txpower``\ ) to the hardware.
    This function may sleep.
    Can be NULL, if (and ONLY if) \ ``recalc_txpower``\  \_always_
    returns B43_TXPWR_RES_DONE.

pwork_15sec
    Periodic work. Called every 15 seconds.
    Can be NULL, if not required.

pwork_60sec
    Periodic work. Called every 60 seconds.
    Can be NULL, if not required.

.. _`b43_phy_allocate`:

b43_phy_allocate
================

.. c:function:: int b43_phy_allocate(struct b43_wldev *dev)

    Allocate PHY structs Allocate the PHY data structures, based on the current dev->phy.type

    :param struct b43_wldev \*dev:
        *undescribed*

.. _`b43_phy_free`:

b43_phy_free
============

.. c:function:: void b43_phy_free(struct b43_wldev *dev)

    Free PHY structs

    :param struct b43_wldev \*dev:
        *undescribed*

.. _`b43_phy_init`:

b43_phy_init
============

.. c:function:: int b43_phy_init(struct b43_wldev *dev)

    Initialise the PHY

    :param struct b43_wldev \*dev:
        *undescribed*

.. _`b43_phy_exit`:

b43_phy_exit
============

.. c:function:: void b43_phy_exit(struct b43_wldev *dev)

    Cleanup PHY

    :param struct b43_wldev \*dev:
        *undescribed*

.. _`b43_has_hardware_pctl`:

b43_has_hardware_pctl
=====================

.. c:function:: bool b43_has_hardware_pctl(struct b43_wldev *dev)

    Hardware Power Control supported? Returns a boolean, whether hardware power control is supported.

    :param struct b43_wldev \*dev:
        *undescribed*

.. _`b43_phy_read`:

b43_phy_read
============

.. c:function:: u16 b43_phy_read(struct b43_wldev *dev, u16 reg)

    16bit PHY register read access

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 reg:
        *undescribed*

.. _`b43_phy_write`:

b43_phy_write
=============

.. c:function:: void b43_phy_write(struct b43_wldev *dev, u16 reg, u16 value)

    16bit PHY register write access

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 reg:
        *undescribed*

    :param u16 value:
        *undescribed*

.. _`b43_phy_copy`:

b43_phy_copy
============

.. c:function:: void b43_phy_copy(struct b43_wldev *dev, u16 destreg, u16 srcreg)

    copy contents of 16bit PHY register to another

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 destreg:
        *undescribed*

    :param u16 srcreg:
        *undescribed*

.. _`b43_phy_mask`:

b43_phy_mask
============

.. c:function:: void b43_phy_mask(struct b43_wldev *dev, u16 offset, u16 mask)

    Mask a PHY register with a mask

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 offset:
        *undescribed*

    :param u16 mask:
        *undescribed*

.. _`b43_phy_set`:

b43_phy_set
===========

.. c:function:: void b43_phy_set(struct b43_wldev *dev, u16 offset, u16 set)

    OR a PHY register with a bitmap

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 offset:
        *undescribed*

    :param u16 set:
        *undescribed*

.. _`b43_phy_maskset`:

b43_phy_maskset
===============

.. c:function:: void b43_phy_maskset(struct b43_wldev *dev, u16 offset, u16 mask, u16 set)

    Mask and OR a PHY register with a mask and bitmap

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 offset:
        *undescribed*

    :param u16 mask:
        *undescribed*

    :param u16 set:
        *undescribed*

.. _`b43_radio_read`:

b43_radio_read
==============

.. c:function:: u16 b43_radio_read(struct b43_wldev *dev, u16 reg)

    16bit Radio register read access

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 reg:
        *undescribed*

.. _`b43_radio_write`:

b43_radio_write
===============

.. c:function:: void b43_radio_write(struct b43_wldev *dev, u16 reg, u16 value)

    16bit Radio register write access

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 reg:
        *undescribed*

    :param u16 value:
        *undescribed*

.. _`b43_radio_mask`:

b43_radio_mask
==============

.. c:function:: void b43_radio_mask(struct b43_wldev *dev, u16 offset, u16 mask)

    Mask a 16bit radio register with a mask

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 offset:
        *undescribed*

    :param u16 mask:
        *undescribed*

.. _`b43_radio_set`:

b43_radio_set
=============

.. c:function:: void b43_radio_set(struct b43_wldev *dev, u16 offset, u16 set)

    OR a 16bit radio register with a bitmap

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 offset:
        *undescribed*

    :param u16 set:
        *undescribed*

.. _`b43_radio_maskset`:

b43_radio_maskset
=================

.. c:function:: void b43_radio_maskset(struct b43_wldev *dev, u16 offset, u16 mask, u16 set)

    Mask and OR a radio register with a mask and bitmap

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 offset:
        *undescribed*

    :param u16 mask:
        *undescribed*

    :param u16 set:
        *undescribed*

.. _`b43_radio_wait_value`:

b43_radio_wait_value
====================

.. c:function:: bool b43_radio_wait_value(struct b43_wldev *dev, u16 offset, u16 mask, u16 value, int delay, int timeout)

    Waits for a given value in masked register read

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 offset:
        *undescribed*

    :param u16 mask:
        *undescribed*

    :param u16 value:
        *undescribed*

    :param int delay:
        *undescribed*

    :param int timeout:
        *undescribed*

.. _`b43_radio_lock`:

b43_radio_lock
==============

.. c:function:: void b43_radio_lock(struct b43_wldev *dev)

    Lock firmware radio register access

    :param struct b43_wldev \*dev:
        *undescribed*

.. _`b43_radio_unlock`:

b43_radio_unlock
================

.. c:function:: void b43_radio_unlock(struct b43_wldev *dev)

    Unlock firmware radio register access

    :param struct b43_wldev \*dev:
        *undescribed*

.. _`b43_phy_lock`:

b43_phy_lock
============

.. c:function:: void b43_phy_lock(struct b43_wldev *dev)

    Lock firmware PHY register access

    :param struct b43_wldev \*dev:
        *undescribed*

.. _`b43_phy_unlock`:

b43_phy_unlock
==============

.. c:function:: void b43_phy_unlock(struct b43_wldev *dev)

    Unlock firmware PHY register access

    :param struct b43_wldev \*dev:
        *undescribed*

.. _`b43_switch_channel`:

b43_switch_channel
==================

.. c:function:: int b43_switch_channel(struct b43_wldev *dev, unsigned int new_channel)

    Switch to another channel

    :param struct b43_wldev \*dev:
        *undescribed*

    :param unsigned int new_channel:
        *undescribed*

.. _`b43_software_rfkill`:

b43_software_rfkill
===================

.. c:function:: void b43_software_rfkill(struct b43_wldev *dev, bool blocked)

    Turn the radio ON or OFF in software.

    :param struct b43_wldev \*dev:
        *undescribed*

    :param bool blocked:
        *undescribed*

.. _`b43_phy_txpower_check`:

b43_phy_txpower_check
=====================

.. c:function:: void b43_phy_txpower_check(struct b43_wldev *dev, unsigned int flags)

    Check TX power output.

    :param struct b43_wldev \*dev:
        *undescribed*

    :param unsigned int flags:
        OR'ed enum b43_phy_txpower_check_flags flags.
        See the docs below.

.. _`b43_phy_txpower_check.description`:

Description
-----------

Compare the current TX power output to the desired power emission
and schedule an adjustment in case it mismatches.

.. _`b43_phy_txpower_check_flags`:

enum b43_phy_txpower_check_flags
================================

.. c:type:: enum b43_phy_txpower_check_flags

    Flags for \ :c:func:`b43_phy_txpower_check`\ 

.. _`b43_phy_txpower_check_flags.definition`:

Definition
----------

.. code-block:: c

    enum b43_phy_txpower_check_flags {
        B43_TXPWR_IGNORE_TIME,
        B43_TXPWR_IGNORE_TSSI
    };

.. _`b43_phy_txpower_check_flags.constants`:

Constants
---------

B43_TXPWR_IGNORE_TIME
    Ignore the schedule time and force-redo
    the check now.

B43_TXPWR_IGNORE_TSSI
    Redo the recalculation, even if the average
    TSSI did not change.

.. _`b43_phy_shm_tssi_read`:

b43_phy_shm_tssi_read
=====================

.. c:function:: int b43_phy_shm_tssi_read(struct b43_wldev *dev, u16 shm_offset)

    Read the average of the last 4 TSSI from SHM.

    :param struct b43_wldev \*dev:
        *undescribed*

    :param u16 shm_offset:
        The SHM address to read the values from.

.. _`b43_phy_shm_tssi_read.description`:

Description
-----------

Returns the average of the 4 TSSI values, or a negative error code.

.. _`b43_phyop_switch_analog_generic`:

b43_phyop_switch_analog_generic
===============================

.. c:function:: void b43_phyop_switch_analog_generic(struct b43_wldev *dev, bool on)

    Generic PHY operation for switching the Analog.

    :param struct b43_wldev \*dev:
        *undescribed*

    :param bool on:
        *undescribed*

.. _`b43_phyop_switch_analog_generic.description`:

Description
-----------

It does the switching based on the PHY0 core register.
Do \_not\_ call this directly. Only use it as a switch_analog callback
for struct b43_phy_operations.

.. This file was automatic generated / don't edit.

