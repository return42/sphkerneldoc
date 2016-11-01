.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/condition.c

.. _`tomoyo_argv`:

tomoyo_argv
===========

.. c:function:: bool tomoyo_argv(const unsigned int index, const char *arg_ptr, const int argc, const struct tomoyo_argv *argv, u8 *checked)

    Check argv[] in "struct linux_binbrm".

    :param const unsigned int index:
        Index number of \ ``arg_ptr``\ .

    :param const char \*arg_ptr:
        Contents of argv[@index].

    :param const int argc:
        Length of \ ``argv``\ .

    :param const struct tomoyo_argv \*argv:
        Pointer to "struct tomoyo_argv".

    :param u8 \*checked:
        Set to true if \ ``argv``\ [@index] was found.

.. _`tomoyo_argv.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_envp`:

tomoyo_envp
===========

.. c:function:: bool tomoyo_envp(const char *env_name, const char *env_value, const int envc, const struct tomoyo_envp *envp, u8 *checked)

    Check envp[] in "struct linux_binbrm".

    :param const char \*env_name:
        The name of environment variable.

    :param const char \*env_value:
        The value of environment variable.

    :param const int envc:
        Length of \ ``envp``\ .

    :param const struct tomoyo_envp \*envp:
        Pointer to "struct tomoyo_envp".

    :param u8 \*checked:
        Set to true if \ ``envp``\ [@env_name] was found.

.. _`tomoyo_envp.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_scan_bprm`:

tomoyo_scan_bprm
================

.. c:function:: bool tomoyo_scan_bprm(struct tomoyo_execve *ee, const u16 argc, const struct tomoyo_argv *argv, const u16 envc, const struct tomoyo_envp *envp)

    Scan "struct linux_binprm".

    :param struct tomoyo_execve \*ee:
        Pointer to "struct tomoyo_execve".

    :param const u16 argc:
        Length of \ ``argc``\ .

    :param const struct tomoyo_argv \*argv:
        Pointer to "struct tomoyo_argv".

    :param const u16 envc:
        Length of \ ``envp``\ .

    :param const struct tomoyo_envp \*envp:
        Poiner to "struct tomoyo_envp".

.. _`tomoyo_scan_bprm.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_scan_exec_realpath`:

tomoyo_scan_exec_realpath
=========================

.. c:function:: bool tomoyo_scan_exec_realpath(struct file *file, const struct tomoyo_name_union *ptr, const bool match)

    Check "exec.realpath" parameter of "struct tomoyo_condition".

    :param struct file \*file:
        Pointer to "struct file".

    :param const struct tomoyo_name_union \*ptr:
        Pointer to "struct tomoyo_name_union".

    :param const bool match:
        True if "exec.realpath=", false if "exec.realpath!=".

.. _`tomoyo_scan_exec_realpath.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_get_dqword`:

tomoyo_get_dqword
=================

.. c:function:: const struct tomoyo_path_info *tomoyo_get_dqword(char *start)

    tomoyo_get_name() for a quoted string.

    :param char \*start:
        String to save.

.. _`tomoyo_get_dqword.description`:

Description
-----------

Returns pointer to "struct tomoyo_path_info" on success, NULL otherwise.

.. _`tomoyo_parse_name_union_quoted`:

tomoyo_parse_name_union_quoted
==============================

.. c:function:: bool tomoyo_parse_name_union_quoted(struct tomoyo_acl_param *param, struct tomoyo_name_union *ptr)

    Parse a quoted word.

    :param struct tomoyo_acl_param \*param:
        Pointer to "struct tomoyo_acl_param".

    :param struct tomoyo_name_union \*ptr:
        Pointer to "struct tomoyo_name_union".

.. _`tomoyo_parse_name_union_quoted.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_parse_argv`:

tomoyo_parse_argv
=================

.. c:function:: bool tomoyo_parse_argv(char *left, char *right, struct tomoyo_argv *argv)

    Parse an argv[] condition part.

    :param char \*left:
        Lefthand value.

    :param char \*right:
        Righthand value.

    :param struct tomoyo_argv \*argv:
        Pointer to "struct tomoyo_argv".

.. _`tomoyo_parse_argv.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_parse_envp`:

tomoyo_parse_envp
=================

.. c:function:: bool tomoyo_parse_envp(char *left, char *right, struct tomoyo_envp *envp)

    Parse an envp[] condition part.

    :param char \*left:
        Lefthand value.

    :param char \*right:
        Righthand value.

    :param struct tomoyo_envp \*envp:
        Pointer to "struct tomoyo_envp".

.. _`tomoyo_parse_envp.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_same_condition`:

tomoyo_same_condition
=====================

.. c:function:: bool tomoyo_same_condition(const struct tomoyo_condition *a, const struct tomoyo_condition *b)

    Check for duplicated "struct tomoyo_condition" entry.

    :param const struct tomoyo_condition \*a:
        Pointer to "struct tomoyo_condition".

    :param const struct tomoyo_condition \*b:
        Pointer to "struct tomoyo_condition".

.. _`tomoyo_same_condition.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_condition_type`:

tomoyo_condition_type
=====================

.. c:function:: u8 tomoyo_condition_type(const char *word)

    Get condition type.

    :param const char \*word:
        Keyword string.

.. _`tomoyo_condition_type.description`:

Description
-----------

Returns one of values in "enum tomoyo_conditions_index" on success,
TOMOYO_MAX_CONDITION_KEYWORD otherwise.

.. _`tomoyo_commit_condition`:

tomoyo_commit_condition
=======================

.. c:function:: struct tomoyo_condition *tomoyo_commit_condition(struct tomoyo_condition *entry)

    Commit "struct tomoyo_condition".

    :param struct tomoyo_condition \*entry:
        Pointer to "struct tomoyo_condition".

.. _`tomoyo_commit_condition.description`:

Description
-----------

Returns pointer to "struct tomoyo_condition" on success, NULL otherwise.

This function merges duplicated entries. This function returns NULL if
\ ``entry``\  is not duplicated but memory quota for policy has exceeded.

.. _`tomoyo_get_transit_preference`:

tomoyo_get_transit_preference
=============================

.. c:function:: char *tomoyo_get_transit_preference(struct tomoyo_acl_param *param, struct tomoyo_condition *e)

    Parse domain transition preference for \ :c:func:`execve`\ .

    :param struct tomoyo_acl_param \*param:
        Pointer to "struct tomoyo_acl_param".

    :param struct tomoyo_condition \*e:
        Pointer to "struct tomoyo_condition".

.. _`tomoyo_get_transit_preference.description`:

Description
-----------

Returns the condition string part.

.. _`tomoyo_get_condition`:

tomoyo_get_condition
====================

.. c:function:: struct tomoyo_condition *tomoyo_get_condition(struct tomoyo_acl_param *param)

    Parse condition part.

    :param struct tomoyo_acl_param \*param:
        Pointer to "struct tomoyo_acl_param".

.. _`tomoyo_get_condition.description`:

Description
-----------

Returns pointer to "struct tomoyo_condition" on success, NULL otherwise.

.. _`tomoyo_get_attributes`:

tomoyo_get_attributes
=====================

.. c:function:: void tomoyo_get_attributes(struct tomoyo_obj_info *obj)

    Revalidate "struct inode".

    :param struct tomoyo_obj_info \*obj:
        Pointer to "struct tomoyo_obj_info".

.. _`tomoyo_get_attributes.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_condition`:

tomoyo_condition
================

.. c:function:: bool tomoyo_condition(struct tomoyo_request_info *r, const struct tomoyo_condition *cond)

    Check condition part.

    :param struct tomoyo_request_info \*r:
        Pointer to "struct tomoyo_request_info".

    :param const struct tomoyo_condition \*cond:
        Pointer to "struct tomoyo_condition". Maybe NULL.

.. _`tomoyo_condition.description`:

Description
-----------

Returns true on success, false otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. This file was automatic generated / don't edit.

