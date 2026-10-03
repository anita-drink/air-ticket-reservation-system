# air-ticket-reservation-system
Full stack web project
**Tools/Languages:** Python, SQL, HTML, Flask, phpMyAdmin

code-documentation -> code manifest.pdf for detailed explanation of all code files

# Security Implementations
* **Prevents SQL injections:** `cursor.execute(sql, (identifier,))` uses %s placeholders and passes user input separately as a tuple. PyMySQL sends the values safely as parameters.
* **Protected Sessions:** sessions do not store sensitive information; airline staff sessions are checked with `get_staff_context()` that queries the DB to fetch staff permissions instead of simply relying on `session["user_type"]`.
* **Timed-out Sessions:** current logged-in session automatically logs out after 3 hours with `App.permanent_session_lifetime = timedelta(hours=3)`.
* **Log-in Attempt Limits:** Limit the number of log-in attempts the user gets to five; prevents brute-force entries.
* **Database Transactions:** Commits and rollbacks for multi-step SQL inserts with `safe_rollback()` helper function; keeps flow atomic (all inserts succeed or none).
