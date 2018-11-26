.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/util.c

.. _`tomoyo_convert_time`:

tomoyo_convert_time
===================

.. c:function:: void tomoyo_convert_time(time64_t time64, struct tomoyo_time *stamp)

    Convert time_t to YYYY/MM/DD hh/mm/ss.

    :param time64:
        *undescribed*
    :type time64: time64_t

    :param stamp:
        Pointer to "struct tomoyo_time".
    :type stamp: struct tomoyo_time \*

.. _`tomoyo_convert_time.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_permstr`:

tomoyo_permstr
==============

.. c:function:: bool tomoyo_permstr(const char *string, const char *keyword)

    Find permission keywords.

    :param string:
        String representation for permissions in foo/bar/buz format.
    :type string: const char \*

    :param keyword:
        Keyword to find from \ ``string``\ /
    :type keyword: const char \*

.. _`tomoyo_permstr.description`:

Description
-----------

Returns ture if \ ``keyword``\  was found in \ ``string``\ , false otherwise.

This function assumes that strncmp(w1, w2, strlen(w1)) != 0 if w1 != w2.

.. _`tomoyo_read_token`:

tomoyo_read_token
=================

.. c:function:: char *tomoyo_read_token(struct tomoyo_acl_param *param)

    Read a word from a line.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

.. _`tomoyo_read_token.description`:

Description
-----------

Returns a word on success, "" otherwise.

To allow the caller to skip NULL check, this function returns "" rather than
NULL if there is no more words to read.

.. _`tomoyo_get_domainname`:

tomoyo_get_domainname
=====================

.. c:function:: const struct tomoyo_path_info *tomoyo_get_domainname(struct tomoyo_acl_param *param)

    Read a domainname from a line.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

.. _`tomoyo_get_domainname.description`:

Description
-----------

Returns a domainname on success, NULL otherwise.

.. _`tomoyo_parse_ulong`:

tomoyo_parse_ulong
==================

.. c:function:: u8 tomoyo_parse_ulong(unsigned long *result, char **str)

    Parse an "unsigned long" value.

    :param result:
        Pointer to "unsigned long".
    :type result: unsigned long \*

    :param str:
        Pointer to string to parse.
    :type str: char \*\*

.. _`tomoyo_parse_ulong.description`:

Description
-----------

Returns one of values in "enum tomoyo_value_type".

The \ ``src``\  is updated to point the first character after the value
on success.

.. _`tomoyo_print_ulong`:

tomoyo_print_ulong
==================

.. c:function:: void tomoyo_print_ulong(char *buffer, const int buffer_len, const unsigned long value, const u8 type)

    Print an "unsigned long" value.

    :param buffer:
        Pointer to buffer.
    :type buffer: char \*

    :param buffer_len:
        Size of \ ``buffer``\ .
    :type buffer_len: const int

    :param value:
        An "unsigned long" value.
    :type value: const unsigned long

    :param type:
        Type of \ ``value``\ .
    :type type: const u8

.. _`tomoyo_print_ulong.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_parse_name_union`:

tomoyo_parse_name_union
=======================

.. c:function:: bool tomoyo_parse_name_union(struct tomoyo_acl_param *param, struct tomoyo_name_union *ptr)

    Parse a tomoyo_name_union.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

    :param ptr:
        Pointer to "struct tomoyo_name_union".
    :type ptr: struct tomoyo_name_union \*

.. _`tomoyo_parse_name_union.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_parse_number_union`:

tomoyo_parse_number_union
=========================

.. c:function:: bool tomoyo_parse_number_union(struct tomoyo_acl_param *param, struct tomoyo_number_union *ptr)

    Parse a tomoyo_number_union.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

    :param ptr:
        Pointer to "struct tomoyo_number_union".
    :type ptr: struct tomoyo_number_union \*

.. _`tomoyo_parse_number_union.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_byte_range`:

tomoyo_byte_range
=================

.. c:function:: bool tomoyo_byte_range(const char *str)

    Check whether the string is a \ooo style octal value.

    :param str:
        Pointer to the string.
    :type str: const char \*

.. _`tomoyo_byte_range.description`:

Description
-----------

Returns true if \ ``str``\  is a \ooo style octal value, false otherwise.

TOMOYO uses \ooo style representation for 0x01 - 0x20 and 0x7F - 0xFF.
This function verifies that \ooo is in valid range.

.. _`tomoyo_alphabet_char`:

tomoyo_alphabet_char
====================

.. c:function:: bool tomoyo_alphabet_char(const char c)

    Check whether the character is an alphabet.

    :param c:
        The character to check.
    :type c: const char

.. _`tomoyo_alphabet_char.description`:

Description
-----------

Returns true if \ ``c``\  is an alphabet character, false otherwise.

.. _`tomoyo_make_byte`:

tomoyo_make_byte
================

.. c:function:: u8 tomoyo_make_byte(const u8 c1, const u8 c2, const u8 c3)

    Make byte value from three octal characters.

    :param c1:
        The first character.
    :type c1: const u8

    :param c2:
        The second character.
    :type c2: const u8

    :param c3:
        The third character.
    :type c3: const u8

.. _`tomoyo_make_byte.description`:

Description
-----------

Returns byte value.

.. _`tomoyo_valid`:

tomoyo_valid
============

.. c:function:: bool tomoyo_valid(const unsigned char c)

    Check whether the character is a valid char.

    :param c:
        The character to check.
    :type c: const unsigned char

.. _`tomoyo_valid.description`:

Description
-----------

Returns true if \ ``c``\  is a valid character, false otherwise.

.. _`tomoyo_invalid`:

tomoyo_invalid
==============

.. c:function:: bool tomoyo_invalid(const unsigned char c)

    Check whether the character is an invalid char.

    :param c:
        The character to check.
    :type c: const unsigned char

.. _`tomoyo_invalid.description`:

Description
-----------

Returns true if \ ``c``\  is an invalid character, false otherwise.

.. _`tomoyo_str_starts`:

tomoyo_str_starts
=================

.. c:function:: bool tomoyo_str_starts(char **src, const char *find)

    Check whether the given string starts with the given keyword.

    :param src:
        Pointer to pointer to the string.
    :type src: char \*\*

    :param find:
        Pointer to the keyword.
    :type find: const char \*

.. _`tomoyo_str_starts.description`:

Description
-----------

Returns true if \ ``src``\  starts with \ ``find``\ , false otherwise.

The \ ``src``\  is updated to point the first character after the \ ``find``\ 
if \ ``src``\  starts with \ ``find``\ .

.. _`tomoyo_normalize_line`:

tomoyo_normalize_line
=====================

.. c:function:: void tomoyo_normalize_line(unsigned char *buffer)

    Format string.

    :param buffer:
        The line to normalize.
    :type buffer: unsigned char \*

.. _`tomoyo_normalize_line.description`:

Description
-----------

Leading and trailing whitespaces are removed.
Multiple whitespaces are packed into single space.

Returns nothing.

.. _`tomoyo_correct_word2`:

tomoyo_correct_word2
====================

.. c:function:: bool tomoyo_correct_word2(const char *string, size_t len)

    Validate a string.

    :param string:
        The string to check. Maybe non-'\0'-terminated.
    :type string: const char \*

    :param len:
        Length of \ ``string``\ .
    :type len: size_t

.. _`tomoyo_correct_word2.description`:

Description
-----------

Check whether the given string follows the naming rules.
Returns true if \ ``string``\  follows the naming rules, false otherwise.

.. _`tomoyo_correct_word`:

tomoyo_correct_word
===================

.. c:function:: bool tomoyo_correct_word(const char *string)

    Validate a string.

    :param string:
        The string to check.
    :type string: const char \*

.. _`tomoyo_correct_word.description`:

Description
-----------

Check whether the given string follows the naming rules.
Returns true if \ ``string``\  follows the naming rules, false otherwise.

.. _`tomoyo_correct_path`:

tomoyo_correct_path
===================

.. c:function:: bool tomoyo_correct_path(const char *filename)

    Validate a pathname.

    :param filename:
        The pathname to check.
    :type filename: const char \*

.. _`tomoyo_correct_path.description`:

Description
-----------

Check whether the given pathname follows the naming rules.
Returns true if \ ``filename``\  follows the naming rules, false otherwise.

.. _`tomoyo_correct_domain`:

tomoyo_correct_domain
=====================

.. c:function:: bool tomoyo_correct_domain(const unsigned char *domainname)

    Check whether the given domainname follows the naming rules.

    :param domainname:
        The domainname to check.
    :type domainname: const unsigned char \*

.. _`tomoyo_correct_domain.description`:

Description
-----------

Returns true if \ ``domainname``\  follows the naming rules, false otherwise.

.. _`tomoyo_domain_def`:

tomoyo_domain_def
=================

.. c:function:: bool tomoyo_domain_def(const unsigned char *buffer)

    Check whether the given token can be a domainname.

    :param buffer:
        The token to check.
    :type buffer: const unsigned char \*

.. _`tomoyo_domain_def.description`:

Description
-----------

Returns true if \ ``buffer``\  possibly be a domainname, false otherwise.

.. _`tomoyo_find_domain`:

tomoyo_find_domain
==================

.. c:function:: struct tomoyo_domain_info *tomoyo_find_domain(const char *domainname)

    Find a domain by the given name.

    :param domainname:
        The domainname to find.
    :type domainname: const char \*

.. _`tomoyo_find_domain.description`:

Description
-----------

Returns pointer to "struct tomoyo_domain_info" if found, NULL otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. _`tomoyo_const_part_length`:

tomoyo_const_part_length
========================

.. c:function:: int tomoyo_const_part_length(const char *filename)

    Evaluate the initial length without a pattern in a token.

    :param filename:
        The string to evaluate.
    :type filename: const char \*

.. _`tomoyo_const_part_length.description`:

Description
-----------

Returns the initial length without a pattern in \ ``filename``\ .

.. _`tomoyo_fill_path_info`:

tomoyo_fill_path_info
=====================

.. c:function:: void tomoyo_fill_path_info(struct tomoyo_path_info *ptr)

    Fill in "struct tomoyo_path_info" members.

    :param ptr:
        Pointer to "struct tomoyo_path_info" to fill in.
    :type ptr: struct tomoyo_path_info \*

.. _`tomoyo_fill_path_info.description`:

Description
-----------

The caller sets "struct tomoyo_path_info"->name.

.. _`tomoyo_file_matches_pattern2`:

tomoyo_file_matches_pattern2
============================

.. c:function:: bool tomoyo_file_matches_pattern2(const char *filename, const char *filename_end, const char *pattern, const char *pattern_end)

    Pattern matching without '/' character and "\-" pattern.

    :param filename:
        The start of string to check.
    :type filename: const char \*

    :param filename_end:
        The end of string to check.
    :type filename_end: const char \*

    :param pattern:
        The start of pattern to compare.
    :type pattern: const char \*

    :param pattern_end:
        The end of pattern to compare.
    :type pattern_end: const char \*

.. _`tomoyo_file_matches_pattern2.description`:

Description
-----------

Returns true if \ ``filename``\  matches \ ``pattern``\ , false otherwise.

.. _`tomoyo_file_matches_pattern`:

tomoyo_file_matches_pattern
===========================

.. c:function:: bool tomoyo_file_matches_pattern(const char *filename, const char *filename_end, const char *pattern, const char *pattern_end)

    Pattern matching without '/' character.

    :param filename:
        The start of string to check.
    :type filename: const char \*

    :param filename_end:
        The end of string to check.
    :type filename_end: const char \*

    :param pattern:
        The start of pattern to compare.
    :type pattern: const char \*

    :param pattern_end:
        The end of pattern to compare.
    :type pattern_end: const char \*

.. _`tomoyo_file_matches_pattern.description`:

Description
-----------

Returns true if \ ``filename``\  matches \ ``pattern``\ , false otherwise.

.. _`tomoyo_path_matches_pattern2`:

tomoyo_path_matches_pattern2
============================

.. c:function:: bool tomoyo_path_matches_pattern2(const char *f, const char *p)

    Do pathname pattern matching.

    :param f:
        The start of string to check.
    :type f: const char \*

    :param p:
        The start of pattern to compare.
    :type p: const char \*

.. _`tomoyo_path_matches_pattern2.description`:

Description
-----------

Returns true if \ ``f``\  matches \ ``p``\ , false otherwise.

.. _`tomoyo_path_matches_pattern`:

tomoyo_path_matches_pattern
===========================

.. c:function:: bool tomoyo_path_matches_pattern(const struct tomoyo_path_info *filename, const struct tomoyo_path_info *pattern)

    Check whether the given filename matches the given pattern.

    :param filename:
        The filename to check.
    :type filename: const struct tomoyo_path_info \*

    :param pattern:
        The pattern to compare.
    :type pattern: const struct tomoyo_path_info \*

.. _`tomoyo_path_matches_pattern.description`:

Description
-----------

Returns true if matches, false otherwise.

The following patterns are available.
\\     \ itself.
\ooo   Octal representation of a byte.
\\*     Zero or more repetitions of characters other than '/'.
@     Zero or more repetitions of characters other than '/' or '.'.
\?     1 byte character other than '/'.
$     One or more repetitions of decimal digits.
\+     1 decimal digit.
\X     One or more repetitions of hexadecimal digits.
\x     1 hexadecimal digit.
\A     One or more repetitions of alphabet characters.
\a     1 alphabet character.

\-     Subtraction operator.

/\{dir\}/   '/' + 'One or more repetitions of dir/' (e.g. /dir/ /dir/dir/
/dir/dir/dir/ ).

.. _`tomoyo_get_exe`:

tomoyo_get_exe
==============

.. c:function:: const char *tomoyo_get_exe( void)

    Get \ :c:func:`tomoyo_realpath`\  of current process.

    :param void:
        no arguments
    :type void: 

.. _`tomoyo_get_exe.description`:

Description
-----------

Returns the \ :c:func:`tomoyo_realpath`\  of current process on success, NULL otherwise.

This function uses \ :c:func:`kzalloc`\ , so the caller must call \ :c:func:`kfree`\ 
if this function didn't return NULL.

.. _`tomoyo_get_mode`:

tomoyo_get_mode
===============

.. c:function:: int tomoyo_get_mode(const struct tomoyo_policy_namespace *ns, const u8 profile, const u8 index)

    Get MAC mode.

    :param ns:
        Pointer to "struct tomoyo_policy_namespace".
    :type ns: const struct tomoyo_policy_namespace \*

    :param profile:
        Profile number.
    :type profile: const u8

    :param index:
        Index number of functionality.
    :type index: const u8

.. _`tomoyo_get_mode.description`:

Description
-----------

Returns mode.

.. _`tomoyo_init_request_info`:

tomoyo_init_request_info
========================

.. c:function:: int tomoyo_init_request_info(struct tomoyo_request_info *r, struct tomoyo_domain_info *domain, const u8 index)

    Initialize "struct tomoyo_request_info" members.

    :param r:
        Pointer to "struct tomoyo_request_info" to initialize.
    :type r: struct tomoyo_request_info \*

    :param domain:
        Pointer to "struct tomoyo_domain_info". NULL for \ :c:func:`tomoyo_domain`\ .
    :type domain: struct tomoyo_domain_info \*

    :param index:
        Index number of functionality.
    :type index: const u8

.. _`tomoyo_init_request_info.description`:

Description
-----------

Returns mode.

.. _`tomoyo_domain_quota_is_ok`:

tomoyo_domain_quota_is_ok
=========================

.. c:function:: bool tomoyo_domain_quota_is_ok(struct tomoyo_request_info *r)

    Check for domain's quota.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

.. _`tomoyo_domain_quota_is_ok.description`:

Description
-----------

Returns true if the domain is not exceeded quota, false otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. This file was automatic generated / don't edit.

