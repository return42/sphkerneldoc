.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/gc.c

.. _`tomoyo_memory_free`:

tomoyo_memory_free
==================

.. c:function:: void tomoyo_memory_free(void *ptr)

    Free memory for elements.

    :param void \*ptr:
        Pointer to allocated memory.

.. _`tomoyo_memory_free.description`:

Description
-----------

Returns nothing.

Caller holds tomoyo_policy_lock mutex.

.. _`tomoyo_struct_used_by_io_buffer`:

tomoyo_struct_used_by_io_buffer
===============================

.. c:function:: bool tomoyo_struct_used_by_io_buffer(const struct list_head *element)

    Check whether the list element is used by /sys/kernel/security/tomoyo/ users or not.

    :param const struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_struct_used_by_io_buffer.description`:

Description
-----------

Returns true if \ ``element``\  is used by /sys/kernel/security/tomoyo/ users,
false otherwise.

.. _`tomoyo_name_used_by_io_buffer`:

tomoyo_name_used_by_io_buffer
=============================

.. c:function:: bool tomoyo_name_used_by_io_buffer(const char *string)

    Check whether the string is used by /sys/kernel/security/tomoyo/ users or not.

    :param const char \*string:
        String to check.

.. _`tomoyo_name_used_by_io_buffer.description`:

Description
-----------

Returns true if \ ``string``\  is used by /sys/kernel/security/tomoyo/ users,
false otherwise.

.. _`tomoyo_del_transition_control`:

tomoyo_del_transition_control
=============================

.. c:function:: void tomoyo_del_transition_control(struct list_head *element)

    Delete members in "struct tomoyo_transition_control".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_transition_control.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_del_aggregator`:

tomoyo_del_aggregator
=====================

.. c:function:: void tomoyo_del_aggregator(struct list_head *element)

    Delete members in "struct tomoyo_aggregator".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_aggregator.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_del_manager`:

tomoyo_del_manager
==================

.. c:function:: void tomoyo_del_manager(struct list_head *element)

    Delete members in "struct tomoyo_manager".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_manager.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_del_acl`:

tomoyo_del_acl
==============

.. c:function:: void tomoyo_del_acl(struct list_head *element)

    Delete members in "struct tomoyo_acl_info".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_acl.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_del_domain`:

tomoyo_del_domain
=================

.. c:function:: void tomoyo_del_domain(struct list_head *element)

    Delete members in "struct tomoyo_domain_info".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_domain.description`:

Description
-----------

Returns nothing.

Caller holds tomoyo_policy_lock mutex.

.. _`tomoyo_del_condition`:

tomoyo_del_condition
====================

.. c:function:: void tomoyo_del_condition(struct list_head *element)

    Delete members in "struct tomoyo_condition".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_condition.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_del_name`:

tomoyo_del_name
===============

.. c:function:: void tomoyo_del_name(struct list_head *element)

    Delete members in "struct tomoyo_name".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_name.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_del_path_group`:

tomoyo_del_path_group
=====================

.. c:function:: void tomoyo_del_path_group(struct list_head *element)

    Delete members in "struct tomoyo_path_group".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_path_group.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_del_group`:

tomoyo_del_group
================

.. c:function:: void tomoyo_del_group(struct list_head *element)

    Delete "struct tomoyo_group".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_group.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_del_address_group`:

tomoyo_del_address_group
========================

.. c:function:: void tomoyo_del_address_group(struct list_head *element)

    Delete members in "struct tomoyo_address_group".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_address_group.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_del_number_group`:

tomoyo_del_number_group
=======================

.. c:function:: void tomoyo_del_number_group(struct list_head *element)

    Delete members in "struct tomoyo_number_group".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_del_number_group.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_try_to_gc`:

tomoyo_try_to_gc
================

.. c:function:: void tomoyo_try_to_gc(const enum tomoyo_policy_id type, struct list_head *element)

    Try to \ :c:func:`kfree`\  an entry.

    :param const enum tomoyo_policy_id type:
        One of values in "enum tomoyo_policy_id".

    :param struct list_head \*element:
        Pointer to "struct list_head".

.. _`tomoyo_try_to_gc.description`:

Description
-----------

Returns nothing.

Caller holds tomoyo_policy_lock mutex.

.. _`tomoyo_collect_member`:

tomoyo_collect_member
=====================

.. c:function:: void tomoyo_collect_member(const enum tomoyo_policy_id id, struct list_head *member_list)

    Delete elements with "struct tomoyo_acl_head".

    :param const enum tomoyo_policy_id id:
        One of values in "enum tomoyo_policy_id".

    :param struct list_head \*member_list:
        Pointer to "struct list_head".

.. _`tomoyo_collect_member.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_collect_acl`:

tomoyo_collect_acl
==================

.. c:function:: void tomoyo_collect_acl(struct list_head *list)

    Delete elements in "struct tomoyo_domain_info".

    :param struct list_head \*list:
        Pointer to "struct list_head".

.. _`tomoyo_collect_acl.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_collect_entry`:

tomoyo_collect_entry
====================

.. c:function:: void tomoyo_collect_entry( void)

    Try to \ :c:func:`kfree`\  deleted elements.

    :param  void:
        no arguments

.. _`tomoyo_collect_entry.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_gc_thread`:

tomoyo_gc_thread
================

.. c:function:: int tomoyo_gc_thread(void *unused)

    Garbage collector thread function.

    :param void \*unused:
        Unused.

.. _`tomoyo_gc_thread.description`:

Description
-----------

Returns 0.

.. _`tomoyo_notify_gc`:

tomoyo_notify_gc
================

.. c:function:: void tomoyo_notify_gc(struct tomoyo_io_buffer *head, const bool is_register)

    Register/unregister /sys/kernel/security/tomoyo/ users.

    :param struct tomoyo_io_buffer \*head:
        Pointer to "struct tomoyo_io_buffer".

    :param const bool is_register:
        True if register, false if unregister.

.. _`tomoyo_notify_gc.description`:

Description
-----------

Returns nothing.

.. This file was automatic generated / don't edit.

