"""
Stripe Atlas — Company Name Check (Practice OA)

Context
-------
Stripe Atlas enables founders to remotely incorporate a US-based company.
Founders propose a company name and Stripe performs internal validation to
ensure the name isn't already in use. Names don't have to be exactly identical
to be considered the same — names that are too similar (and could be confused
for other companies) are disallowed.

Your Task
---------
Complete a program that reads multiple lines from stdin. Each line represents
a name-availability check and has the form:

    <account_id>|<proposed company name>

For each line, output a single line:

    <account_id>|Name Available
or
    <account_id>|Name Not Available

Rules for “same name”
---------------------
Two names are considered the same if, after applying ALL transformations below,
their normalized forms are identical. If, after transformations, the name is
empty or only spaces, it is considered Not Available.

Transformations:
1) Ignore capitalization (case-insensitive comparison).
2) Treat ampersands '&' and commas ',' as spaces.
3) Treat multiple spaces in a row as a single space.
4) Ignore company suffixes at the end (case-insensitive). You may assume every
   name has one suffix, and it is one of:
      ["Inc.", "Corp.", "LLC", "L.L.C."]
5) Ignore a leading article if present: "The", "An", "A".
6) Ignore the word "and" everywhere EXCEPT when it is the very first word of
   the company name. Examples:
      - "Llama And Friend, Inc." == "Llama Friend, Inc."
      - "And Llama Friend, Inc."  is DIFFERENT from "Llama Friend, Inc."

Processing semantics
--------------------
• Process requests in order.
• If a normalized name has not been seen before, print "Name Available" and
  mark it as taken for future requests.
• If a normalized name has been seen before, print "Name Not Available".
• If normalization produces an empty string, print "Name Not Available".

Input
-----
Multiple lines from stdin:
    <account_id>|<proposed company name>

Output
------
For each input line:
    <account_id>|Name Available
or
    <account_id>|Name Not Available

Example
-------
Input:
    acct_12345|Llama Industries, Inc.

Output:
    acct_12345|Name Available
"""
