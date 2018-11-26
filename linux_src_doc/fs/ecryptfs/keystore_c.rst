.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/keystore.c

.. _`process_request_key_err`:

process_request_key_err
=======================

.. c:function:: int process_request_key_err(long err_code)

    Linux filesystem encryption layer In-kernel key management code.  Includes functions to parse and write authentication token-related packets with the underlying file.

    :param err_code:
        *undescribed*
    :type err_code: long

.. _`process_request_key_err.description`:

Description
-----------

Copyright (C) 2004-2006 International Business Machines Corp.
Author(s): Michael A. Halcrow <mhalcrow@us.ibm.com>
Michael C. Thompson <mcthomps@us.ibm.com>
Trevor S. Highland <trevor.highland@gmail.com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
02111-1307, USA.

.. _`ecryptfs_parse_packet_length`:

ecryptfs_parse_packet_length
============================

.. c:function:: int ecryptfs_parse_packet_length(unsigned char *data, size_t *size, size_t *length_size)

    :param data:
        Pointer to memory containing length at offset
    :type data: unsigned char \*

    :param size:
        This function writes the decoded size to this memory
        address; zero on error
    :type size: size_t \*

    :param length_size:
        The number of bytes occupied by the encoded length
    :type length_size: size_t \*

.. _`ecryptfs_parse_packet_length.description`:

Description
-----------

Returns zero on success; non-zero on error

.. _`ecryptfs_write_packet_length`:

ecryptfs_write_packet_length
============================

.. c:function:: int ecryptfs_write_packet_length(char *dest, size_t size, size_t *packet_size_length)

    :param dest:
        The byte array target into which to write the length. Must
        have at least ECRYPTFS_MAX_PKT_LEN_SIZE bytes allocated.
    :type dest: char \*

    :param size:
        The length to write.
    :type size: size_t

    :param packet_size_length:
        The number of bytes used to encode the packet
        length is written to this address.
    :type packet_size_length: size_t \*

.. _`ecryptfs_write_packet_length.description`:

Description
-----------

Returns zero on success; non-zero on error.

.. _`ecryptfs_verify_version`:

ecryptfs_verify_version
=======================

.. c:function:: int ecryptfs_verify_version(u16 version)

    :param version:
        The version number to confirm
    :type version: u16

.. _`ecryptfs_verify_version.description`:

Description
-----------

Returns zero on good version; non-zero otherwise

.. _`ecryptfs_verify_auth_tok_from_key`:

ecryptfs_verify_auth_tok_from_key
=================================

.. c:function:: int ecryptfs_verify_auth_tok_from_key(struct key *auth_tok_key, struct ecryptfs_auth_tok **auth_tok)

    :param auth_tok_key:
        key containing the authentication token
    :type auth_tok_key: struct key \*

    :param auth_tok:
        authentication token
    :type auth_tok: struct ecryptfs_auth_tok \*\*

.. _`ecryptfs_verify_auth_tok_from_key.description`:

Description
-----------

Returns zero on valid auth tok; -EINVAL if the payload is invalid; or
-EKEYREVOKED if the key was revoked before we acquired its semaphore.

.. _`ecryptfs_find_auth_tok_for_sig`:

ecryptfs_find_auth_tok_for_sig
==============================

.. c:function:: int ecryptfs_find_auth_tok_for_sig(struct key **auth_tok_key, struct ecryptfs_auth_tok **auth_tok, struct ecryptfs_mount_crypt_stat *mount_crypt_stat, char *sig)

    :param auth_tok_key:
        *undescribed*
    :type auth_tok_key: struct key \*\*

    :param auth_tok:
        Set to the matching auth_tok; NULL if not found
    :type auth_tok: struct ecryptfs_auth_tok \*\*

    :param mount_crypt_stat:
        *undescribed*
    :type mount_crypt_stat: struct ecryptfs_mount_crypt_stat \*

    :param sig:
        Sig of auth_tok to find
    :type sig: char \*

.. _`ecryptfs_find_auth_tok_for_sig.description`:

Description
-----------

For now, this function simply looks at the registered auth_tok's
linked off the mount_crypt_stat, so all the auth_toks that can be
used must be registered at mount time. This function could
potentially try a lot harder to find auth_tok's (e.g., by calling
out to ecryptfsd to dynamically retrieve an auth_tok object) so
that static registration of auth_tok's will no longer be necessary.

Returns zero on no error; non-zero on error

.. _`ecryptfs_write_tag_70_packet`:

ecryptfs_write_tag_70_packet
============================

.. c:function:: int ecryptfs_write_tag_70_packet(char *dest, size_t *remaining_bytes, size_t *packet_size, struct ecryptfs_mount_crypt_stat *mount_crypt_stat, char *filename, size_t filename_size)

    Write encrypted filename (EFN) packet against FNEK

    :param dest:
        *undescribed*
    :type dest: char \*

    :param remaining_bytes:
        *undescribed*
    :type remaining_bytes: size_t \*

    :param packet_size:
        *undescribed*
    :type packet_size: size_t \*

    :param mount_crypt_stat:
        *undescribed*
    :type mount_crypt_stat: struct ecryptfs_mount_crypt_stat \*

    :param filename:
        NULL-terminated filename string
    :type filename: char \*

    :param filename_size:
        *undescribed*
    :type filename_size: size_t

.. _`ecryptfs_write_tag_70_packet.description`:

Description
-----------

This is the simplest mechanism for achieving filename encryption in
eCryptfs. It encrypts the given filename with the mount-wide
filename encryption key (FNEK) and stores it in a packet to \ ``dest``\ ,
which the callee will encode and write directly into the dentry
name.

.. _`ecryptfs_parse_tag_70_packet`:

ecryptfs_parse_tag_70_packet
============================

.. c:function:: int ecryptfs_parse_tag_70_packet(char **filename, size_t *filename_size, size_t *packet_size, struct ecryptfs_mount_crypt_stat *mount_crypt_stat, char *data, size_t max_packet_size)

    Parse and process FNEK-encrypted passphrase packet

    :param filename:
        This function kmalloc's the memory for the filename
    :type filename: char \*\*

    :param filename_size:
        This function sets this to the amount of memory
        kmalloc'd for the filename
    :type filename_size: size_t \*

    :param packet_size:
        This function sets this to the the number of octets
        in the packet parsed
    :type packet_size: size_t \*

    :param mount_crypt_stat:
        The mount-wide cryptographic context
    :type mount_crypt_stat: struct ecryptfs_mount_crypt_stat \*

    :param data:
        The memory location containing the start of the tag 70
        packet
    :type data: char \*

    :param max_packet_size:
        The maximum legal size of the packet to be parsed
        from \ ``data``\ 
    :type max_packet_size: size_t

.. _`ecryptfs_parse_tag_70_packet.description`:

Description
-----------

Returns zero on success; non-zero otherwise

.. _`decrypt_pki_encrypted_session_key`:

decrypt_pki_encrypted_session_key
=================================

.. c:function:: int decrypt_pki_encrypted_session_key(struct ecryptfs_auth_tok *auth_tok, struct ecryptfs_crypt_stat *crypt_stat)

    Decrypt the session key with the given auth_tok.

    :param auth_tok:
        The key authentication token used to decrypt the session key
    :type auth_tok: struct ecryptfs_auth_tok \*

    :param crypt_stat:
        The cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

.. _`decrypt_pki_encrypted_session_key.description`:

Description
-----------

Returns zero on success; non-zero error otherwise.

.. _`parse_tag_1_packet`:

parse_tag_1_packet
==================

.. c:function:: int parse_tag_1_packet(struct ecryptfs_crypt_stat *crypt_stat, unsigned char *data, struct list_head *auth_tok_list, struct ecryptfs_auth_tok **new_auth_tok, size_t *packet_size, size_t max_packet_size)

    :param crypt_stat:
        The cryptographic context to modify based on packet contents
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param data:
        The raw bytes of the packet.
    :type data: unsigned char \*

    :param auth_tok_list:
        eCryptfs parses packets into authentication tokens;
        a new authentication token will be placed at the
        end of this list for this packet.
    :type auth_tok_list: struct list_head \*

    :param new_auth_tok:
        Pointer to a pointer to memory that this function
        allocates; sets the memory address of the pointer to
        NULL on error. This object is added to the
        auth_tok_list.
    :type new_auth_tok: struct ecryptfs_auth_tok \*\*

    :param packet_size:
        This function writes the size of the parsed packet
        into this memory location; zero on error.
    :type packet_size: size_t \*

    :param max_packet_size:
        The maximum allowable packet size
    :type max_packet_size: size_t

.. _`parse_tag_1_packet.description`:

Description
-----------

Returns zero on success; non-zero on error.

.. _`parse_tag_3_packet`:

parse_tag_3_packet
==================

.. c:function:: int parse_tag_3_packet(struct ecryptfs_crypt_stat *crypt_stat, unsigned char *data, struct list_head *auth_tok_list, struct ecryptfs_auth_tok **new_auth_tok, size_t *packet_size, size_t max_packet_size)

    :param crypt_stat:
        The cryptographic context to modify based on packet
        contents.
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param data:
        The raw bytes of the packet.
    :type data: unsigned char \*

    :param auth_tok_list:
        eCryptfs parses packets into authentication tokens;
        a new authentication token will be placed at the end
        of this list for this packet.
    :type auth_tok_list: struct list_head \*

    :param new_auth_tok:
        Pointer to a pointer to memory that this function
        allocates; sets the memory address of the pointer to
        NULL on error. This object is added to the
        auth_tok_list.
    :type new_auth_tok: struct ecryptfs_auth_tok \*\*

    :param packet_size:
        This function writes the size of the parsed packet
        into this memory location; zero on error.
    :type packet_size: size_t \*

    :param max_packet_size:
        maximum number of bytes to parse
    :type max_packet_size: size_t

.. _`parse_tag_3_packet.description`:

Description
-----------

Returns zero on success; non-zero on error.

.. _`parse_tag_11_packet`:

parse_tag_11_packet
===================

.. c:function:: int parse_tag_11_packet(unsigned char *data, unsigned char *contents, size_t max_contents_bytes, size_t *tag_11_contents_size, size_t *packet_size, size_t max_packet_size)

    :param data:
        The raw bytes of the packet
    :type data: unsigned char \*

    :param contents:
        This function writes the data contents of the literal
        packet into this memory location
    :type contents: unsigned char \*

    :param max_contents_bytes:
        The maximum number of bytes that this function
        is allowed to write into contents
    :type max_contents_bytes: size_t

    :param tag_11_contents_size:
        This function writes the size of the parsed
        contents into this memory location; zero on
        error
    :type tag_11_contents_size: size_t \*

    :param packet_size:
        This function writes the size of the parsed packet
        into this memory location; zero on error
    :type packet_size: size_t \*

    :param max_packet_size:
        maximum number of bytes to parse
    :type max_packet_size: size_t

.. _`parse_tag_11_packet.description`:

Description
-----------

Returns zero on success; non-zero on error.

.. _`decrypt_passphrase_encrypted_session_key`:

decrypt_passphrase_encrypted_session_key
========================================

.. c:function:: int decrypt_passphrase_encrypted_session_key(struct ecryptfs_auth_tok *auth_tok, struct ecryptfs_crypt_stat *crypt_stat)

    Decrypt the session key with the given auth_tok.

    :param auth_tok:
        The passphrase authentication token to use to encrypt the FEK
    :type auth_tok: struct ecryptfs_auth_tok \*

    :param crypt_stat:
        The cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

.. _`decrypt_passphrase_encrypted_session_key.description`:

Description
-----------

Returns zero on success; non-zero error otherwise

.. _`ecryptfs_parse_packet_set`:

ecryptfs_parse_packet_set
=========================

.. c:function:: int ecryptfs_parse_packet_set(struct ecryptfs_crypt_stat *crypt_stat, unsigned char *src, struct dentry *ecryptfs_dentry)

    :param crypt_stat:
        The cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param src:
        Virtual address of region of memory containing the packets
    :type src: unsigned char \*

    :param ecryptfs_dentry:
        The eCryptfs dentry associated with the packet set
    :type ecryptfs_dentry: struct dentry \*

.. _`ecryptfs_parse_packet_set.description`:

Description
-----------

Get crypt_stat to have the file's session key if the requisite key
is available to decrypt the session key.

Returns Zero if a valid authentication token was retrieved and
processed; negative value for file not encrypted or for error
conditions.

.. _`write_tag_1_packet`:

write_tag_1_packet
==================

.. c:function:: int write_tag_1_packet(char *dest, size_t *remaining_bytes, struct key *auth_tok_key, struct ecryptfs_auth_tok *auth_tok, struct ecryptfs_crypt_stat *crypt_stat, struct ecryptfs_key_record *key_rec, size_t *packet_size)

    Write an RFC2440-compatible tag 1 (public key) packet

    :param dest:
        Buffer into which to write the packet
    :type dest: char \*

    :param remaining_bytes:
        Maximum number of bytes that can be writtn
    :type remaining_bytes: size_t \*

    :param auth_tok_key:
        The authentication token key to unlock and put when done with
        \ ``auth_tok``\ 
    :type auth_tok_key: struct key \*

    :param auth_tok:
        The authentication token used for generating the tag 1 packet
    :type auth_tok: struct ecryptfs_auth_tok \*

    :param crypt_stat:
        The cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param key_rec:
        The key record struct for the tag 1 packet
    :type key_rec: struct ecryptfs_key_record \*

    :param packet_size:
        This function will write the number of bytes that end
        up constituting the packet; set to zero on error
    :type packet_size: size_t \*

.. _`write_tag_1_packet.description`:

Description
-----------

Returns zero on success; non-zero on error.

.. _`write_tag_11_packet`:

write_tag_11_packet
===================

.. c:function:: int write_tag_11_packet(char *dest, size_t *remaining_bytes, char *contents, size_t contents_length, size_t *packet_length)

    :param dest:
        Target into which Tag 11 packet is to be written
    :type dest: char \*

    :param remaining_bytes:
        Maximum packet length
    :type remaining_bytes: size_t \*

    :param contents:
        Byte array of contents to copy in
    :type contents: char \*

    :param contents_length:
        Number of bytes in contents
    :type contents_length: size_t

    :param packet_length:
        Length of the Tag 11 packet written; zero on error
    :type packet_length: size_t \*

.. _`write_tag_11_packet.description`:

Description
-----------

Returns zero on success; non-zero on error.

.. _`write_tag_3_packet`:

write_tag_3_packet
==================

.. c:function:: int write_tag_3_packet(char *dest, size_t *remaining_bytes, struct ecryptfs_auth_tok *auth_tok, struct ecryptfs_crypt_stat *crypt_stat, struct ecryptfs_key_record *key_rec, size_t *packet_size)

    :param dest:
        Buffer into which to write the packet
    :type dest: char \*

    :param remaining_bytes:
        Maximum number of bytes that can be written
    :type remaining_bytes: size_t \*

    :param auth_tok:
        Authentication token
    :type auth_tok: struct ecryptfs_auth_tok \*

    :param crypt_stat:
        The cryptographic context
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param key_rec:
        encrypted key
    :type key_rec: struct ecryptfs_key_record \*

    :param packet_size:
        This function will write the number of bytes that end
        up constituting the packet; set to zero on error
    :type packet_size: size_t \*

.. _`write_tag_3_packet.description`:

Description
-----------

Returns zero on success; non-zero on error.

.. _`ecryptfs_generate_key_packet_set`:

ecryptfs_generate_key_packet_set
================================

.. c:function:: int ecryptfs_generate_key_packet_set(char *dest_base, struct ecryptfs_crypt_stat *crypt_stat, struct dentry *ecryptfs_dentry, size_t *len, size_t max)

    :param dest_base:
        Virtual address from which to write the key record set
    :type dest_base: char \*

    :param crypt_stat:
        The cryptographic context from which the
        authentication tokens will be retrieved
    :type crypt_stat: struct ecryptfs_crypt_stat \*

    :param ecryptfs_dentry:
        The dentry, used to retrieve the mount crypt stat
        for the global parameters
    :type ecryptfs_dentry: struct dentry \*

    :param len:
        The amount written
    :type len: size_t \*

    :param max:
        The maximum amount of data allowed to be written
    :type max: size_t

.. _`ecryptfs_generate_key_packet_set.description`:

Description
-----------

Generates a key packet set and writes it to the virtual address
passed in.

Returns zero on success; non-zero on error.

.. This file was automatic generated / don't edit.

