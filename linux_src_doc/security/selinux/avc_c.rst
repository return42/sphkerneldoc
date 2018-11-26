.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/avc.c

.. _`avc_dump_av`:

avc_dump_av
===========

.. c:function:: void avc_dump_av(struct audit_buffer *ab, u16 tclass, u32 av)

    Display an access vector in human-readable form.

    :param ab:
        *undescribed*
    :type ab: struct audit_buffer \*

    :param tclass:
        target security class
    :type tclass: u16

    :param av:
        access vector
    :type av: u32

.. _`avc_dump_query`:

avc_dump_query
==============

.. c:function:: void avc_dump_query(struct audit_buffer *ab, struct selinux_state *state, u32 ssid, u32 tsid, u16 tclass)

    Display a SID pair and a class in human-readable form.

    :param ab:
        *undescribed*
    :type ab: struct audit_buffer \*

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param ssid:
        source security identifier
    :type ssid: u32

    :param tsid:
        target security identifier
    :type tsid: u32

    :param tclass:
        target security class
    :type tclass: u16

.. _`avc_init`:

avc_init
========

.. c:function:: void avc_init( void)

    Initialize the AVC.

    :param void:
        no arguments
    :type void: 

.. _`avc_init.description`:

Description
-----------

Initialize the access vector cache.

.. _`avc_lookup`:

avc_lookup
==========

.. c:function:: struct avc_node *avc_lookup(struct selinux_avc *avc, u32 ssid, u32 tsid, u16 tclass)

    Look up an AVC entry.

    :param avc:
        *undescribed*
    :type avc: struct selinux_avc \*

    :param ssid:
        source security identifier
    :type ssid: u32

    :param tsid:
        target security identifier
    :type tsid: u32

    :param tclass:
        target security class
    :type tclass: u16

.. _`avc_lookup.description`:

Description
-----------

Look up an AVC entry that is valid for the
(@ssid, \ ``tsid``\ ), interpreting the permissions
based on \ ``tclass``\ .  If a valid AVC entry exists,
then this function returns the avc_node.
Otherwise, this function returns NULL.

.. _`avc_insert`:

avc_insert
==========

.. c:function:: struct avc_node *avc_insert(struct selinux_avc *avc, u32 ssid, u32 tsid, u16 tclass, struct av_decision *avd, struct avc_xperms_node *xp_node)

    Insert an AVC entry.

    :param avc:
        *undescribed*
    :type avc: struct selinux_avc \*

    :param ssid:
        source security identifier
    :type ssid: u32

    :param tsid:
        target security identifier
    :type tsid: u32

    :param tclass:
        target security class
    :type tclass: u16

    :param avd:
        resulting av decision
    :type avd: struct av_decision \*

    :param xp_node:
        resulting extended permissions
    :type xp_node: struct avc_xperms_node \*

.. _`avc_insert.description`:

Description
-----------

Insert an AVC entry for the SID pair
(@ssid, \ ``tsid``\ ) and class \ ``tclass``\ .
The access vectors and the sequence number are
normally provided by the security server in
response to a \ :c:func:`security_compute_av`\  call.  If the
sequence number \ ``avd->seqno``\  is not less than the latest
revocation notification, then the function copies
the access vectors into a cache entry, returns
avc_node inserted. Otherwise, this function returns NULL.

.. _`avc_audit_pre_callback`:

avc_audit_pre_callback
======================

.. c:function:: void avc_audit_pre_callback(struct audit_buffer *ab, void *a)

    SELinux specific information will be called by generic audit code

    :param ab:
        the audit buffer
    :type ab: struct audit_buffer \*

    :param a:
        audit_data
    :type a: void \*

.. _`avc_audit_post_callback`:

avc_audit_post_callback
=======================

.. c:function:: void avc_audit_post_callback(struct audit_buffer *ab, void *a)

    SELinux specific information will be called by generic audit code

    :param ab:
        the audit buffer
    :type ab: struct audit_buffer \*

    :param a:
        audit_data
    :type a: void \*

.. _`avc_add_callback`:

avc_add_callback
================

.. c:function:: int avc_add_callback(int (*callback)(u32 event), u32 events)

    Register a callback for security events.

    :param int (\*callback)(u32 event):
        callback function

    :param events:
        security events
    :type events: u32

.. _`avc_add_callback.description`:

Description
-----------

Register a callback function for events in the set \ ``events``\ .
Returns \ ``0``\  on success or -%ENOMEM if insufficient memory
exists to add the callback.

.. _`avc_update_node`:

avc_update_node
===============

.. c:function:: int avc_update_node(struct selinux_avc *avc, u32 event, u32 perms, u8 driver, u8 xperm, u32 ssid, u32 tsid, u16 tclass, u32 seqno, struct extended_perms_decision *xpd, u32 flags)

    :param avc:
        *undescribed*
    :type avc: struct selinux_avc \*

    :param event:
        Updating event
    :type event: u32

    :param perms:
        Permission mask bits
    :type perms: u32

    :param driver:
        *undescribed*
    :type driver: u8

    :param xperm:
        *undescribed*
    :type xperm: u8

    :param ssid:
        identifier of an AVC entry
    :type ssid: u32

    :param tsid:
        *undescribed*
    :type tsid: u32

    :param tclass:
        *undescribed*
    :type tclass: u16

    :param seqno:
        sequence number when decision was made
    :type seqno: u32

    :param xpd:
        extended_perms_decision to be added to the node
    :type xpd: struct extended_perms_decision \*

    :param flags:
        *undescribed*
    :type flags: u32

.. _`avc_update_node.description`:

Description
-----------

if a valid AVC entry doesn't exist,this function returns -ENOENT.
if \ :c:func:`kmalloc`\  called internal returns NULL, this function returns -ENOMEM.
otherwise, this function updates the AVC entry. The original AVC-entry object
will release later by RCU.

.. _`avc_flush`:

avc_flush
=========

.. c:function:: void avc_flush(struct selinux_avc *avc)

    Flush the cache

    :param avc:
        *undescribed*
    :type avc: struct selinux_avc \*

.. _`avc_ss_reset`:

avc_ss_reset
============

.. c:function:: int avc_ss_reset(struct selinux_avc *avc, u32 seqno)

    Flush the cache and revalidate migrated permissions.

    :param avc:
        *undescribed*
    :type avc: struct selinux_avc \*

    :param seqno:
        policy sequence number
    :type seqno: u32

.. _`avc_has_perm_noaudit`:

avc_has_perm_noaudit
====================

.. c:function:: int avc_has_perm_noaudit(struct selinux_state *state, u32 ssid, u32 tsid, u16 tclass, u32 requested, unsigned int flags, struct av_decision *avd)

    Check permissions but perform no auditing.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param ssid:
        source security identifier
    :type ssid: u32

    :param tsid:
        target security identifier
    :type tsid: u32

    :param tclass:
        target security class
    :type tclass: u16

    :param requested:
        requested permissions, interpreted based on \ ``tclass``\ 
    :type requested: u32

    :param flags:
        AVC_STRICT or 0
    :type flags: unsigned int

    :param avd:
        access vector decisions
    :type avd: struct av_decision \*

.. _`avc_has_perm_noaudit.description`:

Description
-----------

Check the AVC to determine whether the \ ``requested``\  permissions are granted
for the SID pair (@ssid, \ ``tsid``\ ), interpreting the permissions
based on \ ``tclass``\ , and call the security server on a cache miss to obtain
a new decision and add it to the cache.  Return a copy of the decisions
in \ ``avd``\ .  Return \ ``0``\  if all \ ``requested``\  permissions are granted,
-%EACCES if any permissions are denied, or another -errno upon
other errors.  This function is typically called by \ :c:func:`avc_has_perm`\ ,
but may also be called directly to separate permission checking from
auditing, e.g. in cases where a lock must be held for the check but
should be released for the auditing.

.. _`avc_has_perm`:

avc_has_perm
============

.. c:function:: int avc_has_perm(struct selinux_state *state, u32 ssid, u32 tsid, u16 tclass, u32 requested, struct common_audit_data *auditdata)

    Check permissions and perform any appropriate auditing.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param ssid:
        source security identifier
    :type ssid: u32

    :param tsid:
        target security identifier
    :type tsid: u32

    :param tclass:
        target security class
    :type tclass: u16

    :param requested:
        requested permissions, interpreted based on \ ``tclass``\ 
    :type requested: u32

    :param auditdata:
        auxiliary audit data
    :type auditdata: struct common_audit_data \*

.. _`avc_has_perm.description`:

Description
-----------

Check the AVC to determine whether the \ ``requested``\  permissions are granted
for the SID pair (@ssid, \ ``tsid``\ ), interpreting the permissions
based on \ ``tclass``\ , and call the security server on a cache miss to obtain
a new decision and add it to the cache.  Audit the granting or denial of
permissions in accordance with the policy.  Return \ ``0``\  if all \ ``requested``\ 
permissions are granted, -%EACCES if any permissions are denied, or
another -errno upon other errors.

.. This file was automatic generated / don't edit.

