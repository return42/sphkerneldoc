.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8712/drv_types.h

.. _`_adapter`:

struct \_adapter
================

.. c:type:: struct _adapter

    the main adapter structure for this device.

.. _`_adapter.definition`:

Definition
----------

.. code-block:: c

    struct _adapter {
        struct dvobj_priv dvobjpriv;
        struct mlme_priv mlmepriv;
        struct cmd_priv cmdpriv;
        struct evt_priv evtpriv;
        struct io_queue *pio_queue;
        struct xmit_priv xmitpriv;
        struct recv_priv recvpriv;
        struct sta_priv stapriv;
        struct security_priv securitypriv;
        struct registry_priv registrypriv;
        struct wlan_acl_pool acl_list;
        struct pwrctrl_priv pwrctrlpriv;
        struct eeprom_priv eeprompriv;
        struct hal_priv halpriv;
        struct led_priv ledpriv;
        struct mp_priv mppriv;
        s32 bDriverStopped;
        s32 bSurpriseRemoved;
        s32 bSuspended;
        u32 IsrContent;
        u32 ImrContent;
        u8 EepromAddressSize;
        u8 hw_init_completed;
        struct task_struct *cmdThread;
        pid_t evtThread;
        struct task_struct *xmitThread;
        pid_t recvThread;
        uint (*dvobj_init)(struct _adapter *adapter);
        void (*dvobj_deinit)(struct _adapter *adapter);
        struct net_device *pnetdev;
        int bup;
        struct net_device_stats stats;
        struct iw_statistics iwstats;
        int pid;
        struct work_struct wkFilterRxFF0;
        u8 blnEnableRxFF0Filter;
        spinlock_t lockRxFF0Filter;
        const struct firmware *fw;
        struct usb_interface *pusb_intf;
        struct mutex mutex_start;
        struct completion rtl8712_fw_ready;
    }

.. _`_adapter.members`:

Members
-------

dvobjpriv
    *undescribed*

mlmepriv
    *undescribed*

cmdpriv
    *undescribed*

evtpriv
    *undescribed*

pio_queue
    *undescribed*

xmitpriv
    *undescribed*

recvpriv
    *undescribed*

stapriv
    *undescribed*

securitypriv
    *undescribed*

registrypriv
    *undescribed*

acl_list
    *undescribed*

pwrctrlpriv
    *undescribed*

eeprompriv
    *undescribed*

halpriv
    *undescribed*

ledpriv
    *undescribed*

mppriv
    *undescribed*

bDriverStopped
    *undescribed*

bSurpriseRemoved
    *undescribed*

bSuspended
    *undescribed*

IsrContent
    *undescribed*

ImrContent
    *undescribed*

EepromAddressSize
    *undescribed*

hw_init_completed
    *undescribed*

cmdThread
    *undescribed*

evtThread
    *undescribed*

xmitThread
    *undescribed*

recvThread
    *undescribed*

dvobj_init
    *undescribed*

dvobj_deinit
    *undescribed*

pnetdev
    *undescribed*

bup
    *undescribed*

stats
    *undescribed*

iwstats
    *undescribed*

pid
    *undescribed*

wkFilterRxFF0
    *undescribed*

blnEnableRxFF0Filter
    *undescribed*

lockRxFF0Filter
    *undescribed*

fw
    *undescribed*

pusb_intf
    *undescribed*

mutex_start
    *undescribed*

rtl8712_fw_ready
    *undescribed*

.. _`_adapter.bup`:

bup
---

True indicates that the interface is up.

.. This file was automatic generated / don't edit.

