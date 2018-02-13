.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/smack/smackfs.c

.. _`smk_netlabel_audit_set`:

smk_netlabel_audit_set
======================

.. c:function:: void smk_netlabel_audit_set(struct netlbl_audit *nap)

    fill a netlbl_audit struct

    :param struct netlbl_audit \*nap:
        structure to fill

.. _`smk_set_access`:

smk_set_access
==============

.. c:function:: int smk_set_access(struct smack_parsed_rule *srp, struct list_head *rule_list, struct mutex *rule_lock, int global)

    add a rule to the rule list or replace an old rule

    :param struct smack_parsed_rule \*srp:
        the rule to add or replace

    :param struct list_head \*rule_list:
        the list of rules

    :param struct mutex \*rule_lock:
        the rule list lock

    :param int global:
        if non-zero, indicates a global rule

.. _`smk_set_access.description`:

Description
-----------

Looks through the current subject/object/access list for
the subject/object pair and replaces the access that was
there. If the pair isn't found add it with the specified
access.

Returns 0 if nothing goes wrong or -ENOMEM if it fails
during the allocation of the new pair to add.

.. _`smk_perm_from_str`:

smk_perm_from_str
=================

.. c:function:: int smk_perm_from_str(const char *string)

    parse smack accesses from a text string

    :param const char \*string:
        a text string that contains a Smack accesses code

.. _`smk_perm_from_str.description`:

Description
-----------

Returns an integer with respective bits set for specified accesses.

.. _`smk_fill_rule`:

smk_fill_rule
=============

.. c:function:: int smk_fill_rule(const char *subject, const char *object, const char *access1, const char *access2, struct smack_parsed_rule *rule, int import, int len)

    Fill Smack rule from strings

    :param const char \*subject:
        subject label string

    :param const char \*object:
        object label string

    :param const char \*access1:
        access string

    :param const char \*access2:
        string with permissions to be removed

    :param struct smack_parsed_rule \*rule:
        Smack rule

    :param int import:
        if non-zero, import labels

    :param int len:
        label length limit

.. _`smk_fill_rule.description`:

Description
-----------

Returns 0 on success, appropriate error code on failure.

.. _`smk_parse_rule`:

smk_parse_rule
==============

.. c:function:: int smk_parse_rule(const char *data, struct smack_parsed_rule *rule, int import)

    parse Smack rule from load string

    :param const char \*data:
        string to be parsed whose size is SMK_LOADLEN

    :param struct smack_parsed_rule \*rule:
        Smack rule

    :param int import:
        if non-zero, import labels

.. _`smk_parse_rule.description`:

Description
-----------

Returns 0 on success, -1 on errors.

.. _`smk_parse_long_rule`:

smk_parse_long_rule
===================

.. c:function:: ssize_t smk_parse_long_rule(char *data, struct smack_parsed_rule *rule, int import, int tokens)

    parse Smack rule from rule string

    :param char \*data:
        string to be parsed, null terminated

    :param struct smack_parsed_rule \*rule:
        Will be filled with Smack parsed rule

    :param int import:
        if non-zero, import labels

    :param int tokens:
        numer of substrings expected in data

.. _`smk_parse_long_rule.description`:

Description
-----------

Returns number of processed bytes on success, -ERRNO on failure.

.. _`smk_write_rules_list`:

smk_write_rules_list
====================

.. c:function:: ssize_t smk_write_rules_list(struct file *file, const char __user *buf, size_t count, loff_t *ppos, struct list_head *rule_list, struct mutex *rule_lock, int format)

    \ :c:func:`write`\  for any /smack rule file

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

    :param struct list_head \*rule_list:
        the list of rules to write to

    :param struct mutex \*rule_lock:
        lock for the rule list

    :param int format:
        /smack/load or /smack/load2 or /smack/change-rule format.

.. _`smk_write_rules_list.description`:

Description
-----------

Get one smack access rule from above.

.. _`smk_write_rules_list.the-format-for-smk_long_fmt-is`:

The format for SMK_LONG_FMT is
------------------------------

"subject<whitespace>object<whitespace>access[<whitespace>...]"

.. _`smk_write_rules_list.the-format-for-smk_fixed24_fmt-is-exactly`:

The format for SMK_FIXED24_FMT is exactly
-----------------------------------------

"subject                 object                  rwxat"

.. _`smk_write_rules_list.the-format-for-smk_change_fmt-is`:

The format for SMK_CHANGE_FMT is
--------------------------------

"subject<whitespace>object<whitespace>
acc_enable<whitespace>acc_disable[<whitespace>...]"

.. _`smk_open_load`:

smk_open_load
=============

.. c:function:: int smk_open_load(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /smack/load

    :param struct inode \*inode:
        inode structure representing file

    :param struct file \*file:
        "load" file pointer

.. _`smk_open_load.description`:

Description
-----------

For reading, use load_seq\_\* seq_file reading operations.

.. _`smk_write_load`:

smk_write_load
==============

.. c:function:: ssize_t smk_write_load(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/load

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

.. _`smk_cipso_doi`:

smk_cipso_doi
=============

.. c:function:: void smk_cipso_doi( void)

    initialize the CIPSO domain

    :param  void:
        no arguments

.. _`smk_unlbl_ambient`:

smk_unlbl_ambient
=================

.. c:function:: void smk_unlbl_ambient(char *oldambient)

    initialize the unlabeled domain

    :param char \*oldambient:
        previous domain string

.. _`smk_open_cipso`:

smk_open_cipso
==============

.. c:function:: int smk_open_cipso(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /smack/cipso

    :param struct inode \*inode:
        inode structure representing file

    :param struct file \*file:
        "cipso" file pointer

.. _`smk_open_cipso.description`:

Description
-----------

Connect our cipso_seq\_\* operations with /smack/cipso
file_operations

.. _`smk_set_cipso`:

smk_set_cipso
=============

.. c:function:: ssize_t smk_set_cipso(struct file *file, const char __user *buf, size_t count, loff_t *ppos, int format)

    do the work for \ :c:func:`write`\  for cipso and cipso2

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

    :param int format:
        /smack/cipso or /smack/cipso2

.. _`smk_set_cipso.description`:

Description
-----------

Accepts only one cipso rule per write call.
Returns number of bytes written or error code, as appropriate

.. _`smk_write_cipso`:

smk_write_cipso
===============

.. c:function:: ssize_t smk_write_cipso(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/cipso

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_cipso.description`:

Description
-----------

Accepts only one cipso rule per write call.
Returns number of bytes written or error code, as appropriate

.. _`smk_open_cipso2`:

smk_open_cipso2
===============

.. c:function:: int smk_open_cipso2(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /smack/cipso2

    :param struct inode \*inode:
        inode structure representing file

    :param struct file \*file:
        "cipso2" file pointer

.. _`smk_open_cipso2.description`:

Description
-----------

Connect our cipso_seq\_\* operations with /smack/cipso2
file_operations

.. _`smk_write_cipso2`:

smk_write_cipso2
================

.. c:function:: ssize_t smk_write_cipso2(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/cipso2

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_cipso2.description`:

Description
-----------

Accepts only one cipso rule per write call.
Returns number of bytes written or error code, as appropriate

.. _`smk_open_net4addr`:

smk_open_net4addr
=================

.. c:function:: int smk_open_net4addr(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /smack/netlabel

    :param struct inode \*inode:
        inode structure representing file

    :param struct file \*file:
        "netlabel" file pointer

.. _`smk_open_net4addr.description`:

Description
-----------

Connect our net4addr_seq\_\* operations with /smack/netlabel
file_operations

.. _`smk_net4addr_insert`:

smk_net4addr_insert
===================

.. c:function:: void smk_net4addr_insert(struct smk_net4addr *new)

    :param struct smk_net4addr \*new:
        netlabel to insert

.. _`smk_net4addr_insert.description`:

Description
-----------

This helper insert netlabel in the smack_net4addrs list
sorted by netmask length (longest to smallest)
locked by \ :c:type:`struct smk_net4addr_lock <smk_net4addr_lock>`\  in smk_write_net4addr

.. _`smk_write_net4addr`:

smk_write_net4addr
==================

.. c:function:: ssize_t smk_write_net4addr(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/netlabel

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_net4addr.description`:

Description
-----------

Accepts only one net4addr per write call.
Returns number of bytes written or error code, as appropriate

.. _`smk_open_net6addr`:

smk_open_net6addr
=================

.. c:function:: int smk_open_net6addr(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /smack/netlabel

    :param struct inode \*inode:
        inode structure representing file

    :param struct file \*file:
        "netlabel" file pointer

.. _`smk_open_net6addr.description`:

Description
-----------

Connect our net6addr_seq\_\* operations with /smack/netlabel
file_operations

.. _`smk_net6addr_insert`:

smk_net6addr_insert
===================

.. c:function:: void smk_net6addr_insert(struct smk_net6addr *new)

    :param struct smk_net6addr \*new:
        entry to insert

.. _`smk_net6addr_insert.description`:

Description
-----------

This inserts an entry in the smack_net6addrs list
sorted by netmask length (longest to smallest)
locked by \ :c:type:`struct smk_net6addr_lock <smk_net6addr_lock>`\  in smk_write_net6addr

.. _`smk_write_net6addr`:

smk_write_net6addr
==================

.. c:function:: ssize_t smk_write_net6addr(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/netlabel

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_net6addr.description`:

Description
-----------

Accepts only one net6addr per write call.
Returns number of bytes written or error code, as appropriate

.. _`smk_read_doi`:

smk_read_doi
============

.. c:function:: ssize_t smk_read_doi(struct file *filp, char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`read`\  for /smack/doi

    :param struct file \*filp:
        file pointer, not actually used

    :param char __user \*buf:
        where to put the result

    :param size_t count:
        maximum to send along

    :param loff_t \*ppos:
        where to start

.. _`smk_read_doi.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`smk_write_doi`:

smk_write_doi
=============

.. c:function:: ssize_t smk_write_doi(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/doi

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_doi.description`:

Description
-----------

Returns number of bytes written or error code, as appropriate

.. _`smk_read_direct`:

smk_read_direct
===============

.. c:function:: ssize_t smk_read_direct(struct file *filp, char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`read`\  for /smack/direct

    :param struct file \*filp:
        file pointer, not actually used

    :param char __user \*buf:
        where to put the result

    :param size_t count:
        maximum to send along

    :param loff_t \*ppos:
        where to start

.. _`smk_read_direct.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`smk_write_direct`:

smk_write_direct
================

.. c:function:: ssize_t smk_write_direct(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/direct

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_direct.description`:

Description
-----------

Returns number of bytes written or error code, as appropriate

.. _`smk_read_mapped`:

smk_read_mapped
===============

.. c:function:: ssize_t smk_read_mapped(struct file *filp, char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`read`\  for /smack/mapped

    :param struct file \*filp:
        file pointer, not actually used

    :param char __user \*buf:
        where to put the result

    :param size_t count:
        maximum to send along

    :param loff_t \*ppos:
        where to start

.. _`smk_read_mapped.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`smk_write_mapped`:

smk_write_mapped
================

.. c:function:: ssize_t smk_write_mapped(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/mapped

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_mapped.description`:

Description
-----------

Returns number of bytes written or error code, as appropriate

.. _`smk_read_ambient`:

smk_read_ambient
================

.. c:function:: ssize_t smk_read_ambient(struct file *filp, char __user *buf, size_t cn, loff_t *ppos)

    \ :c:func:`read`\  for /smack/ambient

    :param struct file \*filp:
        file pointer, not actually used

    :param char __user \*buf:
        where to put the result

    :param size_t cn:
        maximum to send along

    :param loff_t \*ppos:
        where to start

.. _`smk_read_ambient.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`smk_write_ambient`:

smk_write_ambient
=================

.. c:function:: ssize_t smk_write_ambient(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/ambient

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_ambient.description`:

Description
-----------

Returns number of bytes written or error code, as appropriate

.. _`smk_list_swap_rcu`:

smk_list_swap_rcu
=================

.. c:function:: void smk_list_swap_rcu(struct list_head *public, struct list_head *private)

    swap public list with a private one in RCU-safe way The caller must hold appropriate mutex to prevent concurrent modifications to the public list. Private list is assumed to be not accessible to other threads yet.

    :param struct list_head \*public:
        public list

    :param struct list_head \*private:
        private list

.. _`smk_parse_label_list`:

smk_parse_label_list
====================

.. c:function:: int smk_parse_label_list(char *data, struct list_head *list)

    parse list of Smack labels, separated by spaces

    :param char \*data:
        the string to parse

    :param struct list_head \*list:
        *undescribed*

.. _`smk_parse_label_list.description`:

Description
-----------

Returns zero on success or error code, as appropriate

.. _`smk_destroy_label_list`:

smk_destroy_label_list
======================

.. c:function:: void smk_destroy_label_list(struct list_head *list)

    destroy a list of smack_known_list_elem

    :param struct list_head \*list:
        *undescribed*

.. _`smk_write_onlycap`:

smk_write_onlycap
=================

.. c:function:: ssize_t smk_write_onlycap(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for smackfs/onlycap

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_onlycap.description`:

Description
-----------

Returns number of bytes written or error code, as appropriate

.. _`smk_read_unconfined`:

smk_read_unconfined
===================

.. c:function:: ssize_t smk_read_unconfined(struct file *filp, char __user *buf, size_t cn, loff_t *ppos)

    \ :c:func:`read`\  for smackfs/unconfined

    :param struct file \*filp:
        file pointer, not actually used

    :param char __user \*buf:
        where to put the result

    :param size_t cn:
        maximum to send along

    :param loff_t \*ppos:
        where to start

.. _`smk_read_unconfined.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`smk_write_unconfined`:

smk_write_unconfined
====================

.. c:function:: ssize_t smk_write_unconfined(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for smackfs/unconfined

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_unconfined.description`:

Description
-----------

Returns number of bytes written or error code, as appropriate

.. _`smk_read_logging`:

smk_read_logging
================

.. c:function:: ssize_t smk_read_logging(struct file *filp, char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`read`\  for /smack/logging

    :param struct file \*filp:
        file pointer, not actually used

    :param char __user \*buf:
        where to put the result

    :param size_t count:
        *undescribed*

    :param loff_t \*ppos:
        where to start

.. _`smk_read_logging.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`smk_write_logging`:

smk_write_logging
=================

.. c:function:: ssize_t smk_write_logging(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/logging

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_logging.description`:

Description
-----------

Returns number of bytes written or error code, as appropriate

.. _`smk_open_load_self`:

smk_open_load_self
==================

.. c:function:: int smk_open_load_self(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /smack/load-self2

    :param struct inode \*inode:
        inode structure representing file

    :param struct file \*file:
        "load" file pointer

.. _`smk_open_load_self.description`:

Description
-----------

For reading, use load_seq\_\* seq_file reading operations.

.. _`smk_write_load_self`:

smk_write_load_self
===================

.. c:function:: ssize_t smk_write_load_self(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/load-self

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

.. _`smk_user_access`:

smk_user_access
===============

.. c:function:: ssize_t smk_user_access(struct file *file, const char __user *buf, size_t count, loff_t *ppos, int format)

    handle access check transaction

    :param struct file \*file:
        file pointer

    :param const char __user \*buf:
        data from user space

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

    :param int format:
        *undescribed*

.. _`smk_write_access`:

smk_write_access
================

.. c:function:: ssize_t smk_write_access(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    handle access check transaction

    :param struct file \*file:
        file pointer

    :param const char __user \*buf:
        data from user space

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

.. _`smk_open_load2`:

smk_open_load2
==============

.. c:function:: int smk_open_load2(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /smack/load2

    :param struct inode \*inode:
        inode structure representing file

    :param struct file \*file:
        "load2" file pointer

.. _`smk_open_load2.description`:

Description
-----------

For reading, use load2_seq\_\* seq_file reading operations.

.. _`smk_write_load2`:

smk_write_load2
===============

.. c:function:: ssize_t smk_write_load2(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/load2

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

.. _`smk_open_load_self2`:

smk_open_load_self2
===================

.. c:function:: int smk_open_load_self2(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /smack/load-self2

    :param struct inode \*inode:
        inode structure representing file

    :param struct file \*file:
        "load" file pointer

.. _`smk_open_load_self2.description`:

Description
-----------

For reading, use load_seq\_\* seq_file reading operations.

.. _`smk_write_load_self2`:

smk_write_load_self2
====================

.. c:function:: ssize_t smk_write_load_self2(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/load-self2

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

.. _`smk_write_access2`:

smk_write_access2
=================

.. c:function:: ssize_t smk_write_access2(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    handle access check transaction

    :param struct file \*file:
        file pointer

    :param const char __user \*buf:
        data from user space

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

.. _`smk_write_revoke_subj`:

smk_write_revoke_subj
=====================

.. c:function:: ssize_t smk_write_revoke_subj(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/revoke-subject

    :param struct file \*file:
        file pointer

    :param const char __user \*buf:
        data from user space

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

.. _`smk_init_sysfs`:

smk_init_sysfs
==============

.. c:function:: int smk_init_sysfs( void)

    initialize /sys/fs/smackfs

    :param  void:
        no arguments

.. _`smk_write_change_rule`:

smk_write_change_rule
=====================

.. c:function:: ssize_t smk_write_change_rule(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/change-rule

    :param struct file \*file:
        file pointer

    :param const char __user \*buf:
        data from user space

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

.. _`smk_read_syslog`:

smk_read_syslog
===============

.. c:function:: ssize_t smk_read_syslog(struct file *filp, char __user *buf, size_t cn, loff_t *ppos)

    \ :c:func:`read`\  for smackfs/syslog

    :param struct file \*filp:
        file pointer, not actually used

    :param char __user \*buf:
        where to put the result

    :param size_t cn:
        maximum to send along

    :param loff_t \*ppos:
        where to start

.. _`smk_read_syslog.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`smk_write_syslog`:

smk_write_syslog
================

.. c:function:: ssize_t smk_write_syslog(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for smackfs/syslog

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start

.. _`smk_write_syslog.description`:

Description
-----------

Returns number of bytes written or error code, as appropriate

.. _`smk_open_relabel_self`:

smk_open_relabel_self
=====================

.. c:function:: int smk_open_relabel_self(struct inode *inode, struct file *file)

    \ :c:func:`open`\  for /smack/relabel-self

    :param struct inode \*inode:
        inode structure representing file

    :param struct file \*file:
        "relabel-self" file pointer

.. _`smk_open_relabel_self.description`:

Description
-----------

Connect our relabel_self_seq\_\* operations with /smack/relabel-self
file_operations

.. _`smk_write_relabel_self`:

smk_write_relabel_self
======================

.. c:function:: ssize_t smk_write_relabel_self(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/relabel-self

    :param struct file \*file:
        file pointer, not actually used

    :param const char __user \*buf:
        where to get the data from

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

.. _`smk_read_ptrace`:

smk_read_ptrace
===============

.. c:function:: ssize_t smk_read_ptrace(struct file *filp, char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`read`\  for /smack/ptrace

    :param struct file \*filp:
        file pointer, not actually used

    :param char __user \*buf:
        where to put the result

    :param size_t count:
        maximum to send along

    :param loff_t \*ppos:
        where to start

.. _`smk_read_ptrace.description`:

Description
-----------

Returns number of bytes read or error code, as appropriate

.. _`smk_write_ptrace`:

smk_write_ptrace
================

.. c:function:: ssize_t smk_write_ptrace(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    \ :c:func:`write`\  for /smack/ptrace

    :param struct file \*file:
        file pointer

    :param const char __user \*buf:
        data from user space

    :param size_t count:
        bytes sent

    :param loff_t \*ppos:
        where to start - must be 0

.. _`smk_fill_super`:

smk_fill_super
==============

.. c:function:: int smk_fill_super(struct super_block *sb, void *data, int silent)

    fill the smackfs superblock

    :param struct super_block \*sb:
        the empty superblock

    :param void \*data:
        unused

    :param int silent:
        unused

.. _`smk_fill_super.description`:

Description
-----------

Fill in the well known entries for the smack filesystem

Returns 0 on success, an error code on failure

.. _`smk_mount`:

smk_mount
=========

.. c:function:: struct dentry *smk_mount(struct file_system_type *fs_type, int flags, const char *dev_name, void *data)

    get the smackfs superblock

    :param struct file_system_type \*fs_type:
        passed along without comment

    :param int flags:
        passed along without comment

    :param const char \*dev_name:
        passed along without comment

    :param void \*data:
        passed along without comment

.. _`smk_mount.description`:

Description
-----------

Just passes everything along.

Returns what the lower level code does.

.. _`init_smk_fs`:

init_smk_fs
===========

.. c:function:: int init_smk_fs( void)

    get the smackfs superblock

    :param  void:
        no arguments

.. _`init_smk_fs.description`:

Description
-----------

register the smackfs

Do not register smackfs if Smack wasn't enabled
on boot. We can not put this method normally under the
\ :c:func:`smack_init`\  code path since the security subsystem get
initialized before the vfs caches.

Returns true if we were not chosen on boot or if
we were chosen and filesystem registration succeeded.

.. This file was automatic generated / don't edit.

