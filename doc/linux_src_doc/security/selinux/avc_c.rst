.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/avc.c

.. _`avc_dump_av`:

avc_dump_av
===========

.. c:function:: void avc_dump_av(struct audit_buffer *ab, u16 tclass, u32 av)

    Display an access vector in human-readable form.

    :param struct audit_buffer \*ab:
        *undescribed*

    :param u16 tclass:
        target security class

    :param u32 av:
        access vector

.. _`avc_dump_query`:

avc_dump_query
==============

.. c:function:: void avc_dump_query(struct audit_buffer *ab, u32 ssid, u32 tsid, u16 tclass)

    Display a SID pair and a class in human-readable form.

    :param struct audit_buffer \*ab:
        *undescribed*

    :param u32 ssid:
        source security identifier

    :param u32 tsid:
        target security identifier

    :param u16 tclass:
        target security class

.. _`avc_init`:

avc_init
========

.. c:function:: void avc_init( void)

    Initialize the AVC.

    :param  void:
        no arguments

.. _`avc_init.description`:

Description
-----------

Initialize the access vector cache.

.. _`avc_lookup`:

avc_lookup
==========

.. c:function:: struct avc_node *avc_lookup(u32 ssid, u32 tsid, u16 tclass)

    Look up an AVC entry.

    :param u32 ssid:
        source security identifier

    :param u32 tsid:
        target security identifier

    :param u16 tclass:
        target security class

.. _`avc_lookup.description`:

Description
-----------

Look up an AVC entry that is valid for the
(\ ``ssid``\ , \ ``tsid``\ ), interpreting the permissions
based on \ ``tclass``\ .  If a valid AVC entry exists,
then this function returns the avc_node.
Otherwise, this function returns NULL.

.. _`avc_insert`:

avc_insert
==========

.. c:function:: struct avc_node *avc_insert(u32 ssid, u32 tsid, u16 tclass, struct av_decision *avd, struct avc_xperms_node *xp_node)

    Insert an AVC entry.

    :param u32 ssid:
        source security identifier

    :param u32 tsid:
        target security identifier

    :param u16 tclass:
        target security class

    :param struct av_decision \*avd:
        resulting av decision

    :param struct avc_xperms_node \*xp_node:
        resulting extended permissions

.. _`avc_insert.description`:

Description
-----------

Insert an AVC entry for the SID pair
(\ ``ssid``\ , \ ``tsid``\ ) and class \ ``tclass``\ .
The access vectors and the sequence number are
normally provided by the security server in
response to a \ :c:func:`security_compute_av`\  call.  If the
sequence number \ ``avd``\ ->seqno is not less than the latest
revocation notification, then the function copies
the access vectors into a cache entry, returns
avc_node inserted. Otherwise, this function returns NULL.

.. _`avc_audit_pre_callback`:

avc_audit_pre_callback
======================

.. c:function:: void avc_audit_pre_callback(struct audit_buffer *ab, void *a)

    SELinux specific information will be called by generic audit code

    :param struct audit_buffer \*ab:
        the audit buffer

    :param void \*a:
        audit_data

.. _`avc_audit_post_callback`:

avc_audit_post_callback
=======================

.. c:function:: void avc_audit_post_callback(struct audit_buffer *ab, void *a)

    SELinux specific information will be called by generic audit code

    :param struct audit_buffer \*ab:
        the audit buffer

    :param void \*a:
        audit_data

.. _`avc_add_callback`:

avc_add_callback
================

.. c:function:: int avc_add_callback(int (*callback)(u32 event), u32 events)

    Register a callback for security events.

    :param int (\*callback)(u32 event):
        callback function

    :param u32 events:
        security events

.. _`avc_add_callback.description`:

Description
-----------

Register a callback function for events in the set \ ``events``\ .
Returns \ ``0``\  on success or -\ ``ENOMEM``\  if insufficient memory
exists to add the callback.

.. _`avc_update_node`:

avc_update_node
===============

.. c:function:: int avc_update_node(u32 event, u32 perms, u8 driver, u8 xperm, u32 ssid, u32 tsid, u16 tclass, u32 seqno, struct extended_perms_decision *xpd, u32 flags)

    :param u32 event:
        Updating event

    :param u32 perms:
        Permission mask bits

    :param u8 driver:
        *undescribed*

    :param u8 xperm:
        *undescribed*

    :param u32 ssid:
        identifier of an AVC entry

    :param u32 tsid:
        *undescribed*

    :param u16 tclass:
        *undescribed*

    :param u32 seqno:
        sequence number when decision was made

    :param struct extended_perms_decision \*xpd:
        extended_perms_decision to be added to the node

    :param u32 flags:
        *undescribed*

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

.. c:function:: void avc_flush( void)

    Flush the cache

    :param  void:
        no arguments

.. _`avc_ss_reset`:

avc_ss_reset
============

.. c:function:: int avc_ss_reset(u32 seqno)

    Flush the cache and revalidate migrated permissions.

    :param u32 seqno:
        policy sequence number

.. _`avc_has_perm_noaudit`:

avc_has_perm_noaudit
====================

.. c:function:: int avc_has_perm_noaudit(u32 ssid, u32 tsid, u16 tclass, u32 requested, unsigned flags, struct av_decision *avd)

    Check permissions but perform no auditing.

    :param u32 ssid:
        source security identifier

    :param u32 tsid:
        target security identifier

    :param u16 tclass:
        target security class

    :param u32 requested:
        requested permissions, interpreted based on \ ``tclass``\ 

    :param unsigned flags:
        AVC_STRICT or 0

    :param struct av_decision \*avd:
        access vector decisions

.. _`avc_has_perm_noaudit.description`:

Description
-----------

Check the AVC to determine whether the \ ``requested``\  permissions are granted
for the SID pair (\ ``ssid``\ , \ ``tsid``\ ), interpreting the permissions
based on \ ``tclass``\ , and call the security server on a cache miss to obtain
a new decision and add it to the cache.  Return a copy of the decisions
in \ ``avd``\ .  Return \ ``0``\  if all \ ``requested``\  permissions are granted,
-\ ``EACCES``\  if any permissions are denied, or another -errno upon
other errors.  This function is typically called by \ :c:func:`avc_has_perm`\ ,
but may also be called directly to separate permission checking from
auditing, e.g. in cases where a lock must be held for the check but
should be released for the auditing.

.. _`avc_has_perm`:

avc_has_perm
============

.. c:function:: int avc_has_perm(u32 ssid, u32 tsid, u16 tclass, u32 requested, struct common_audit_data *auditdata)

    Check permissions and perform any appropriate auditing.

    :param u32 ssid:
        source security identifier

    :param u32 tsid:
        target security identifier

    :param u16 tclass:
        target security class

    :param u32 requested:
        requested permissions, interpreted based on \ ``tclass``\ 

    :param struct common_audit_data \*auditdata:
        auxiliary audit data

.. _`avc_has_perm.description`:

Description
-----------

Check the AVC to determine whether the \ ``requested``\  permissions are granted
for the SID pair (\ ``ssid``\ , \ ``tsid``\ ), interpreting the permissions
based on \ ``tclass``\ , and call the security server on a cache miss to obtain
a new decision and add it to the cache.  Audit the granting or denial of
permissions in accordance with the policy.  Return \ ``0``\  if all \ ``requested``\ 
permissions are granted, -\ ``EACCES``\  if any permissions are denied, or
another -errno upon other errors.

.. This file was automatic generated / don't edit.

