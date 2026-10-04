MCP_SERVERS = {
    "Elasticsearch": {
        "description": "Interact with your Elasticsearch logs and indices through natural language conversations.",
        "tools": {
            "list_indices": "Lists all available Elasticsearch indices in the cluster.",
            "get_mappings": "Gets the structural field mappings and data types for a specific index.",
            "search": "Executes complex data searches using Elasticsearch Query DSL.",
            "esql": "Executes direct ES|QL queries for advanced analytics and logging analysis."
        }
    },

    "Context7": {
        "description": "Pull up-to-date, version-specific documentation and code examples for any library or framework straight into your prompt.",
        "tools": {
            "resolve-library-id": "Resolves a generic library or framework name into a standardized Context7 library ID.",
            "query-docs": "Queries live, version-specific documentation using a validated library ID."
        }
    },

    "MongoDB": {
        "description": "A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.",
        "tools": {
            "list_databases": "Lists all databases available on the connected MongoDB instance.",
            "list_collections": "Lists all collections inside a specified database.",
            "get_schema": "Infers and returns the data schema and document structure of a collection.",
            "find_documents": "Queries and retrieves documents from a collection matching specified filters.",
            "insert_document": "Inserts a new document into a specified collection.",
            "update_documents": "Modifies existing documents that match a query filter.",
            "delete_documents": "Removes documents from a collection based on a filter.",
            "aggregate": "Executes a MongoDB aggregation pipeline for data transformation and analytics.",
            "atlas_get_cluster": "Retrieves the status, configuration, and details of a MongoDB Atlas cluster.",
            "atlas_scale_cluster": "Dynamically scales Atlas cluster tiers, storage, or instance sizes."
        }
    },

    "Perplexity": {
        "description": "Connector for Perplexity API, to enable real-time, web-wide research.",
        "tools": {
            "perplexity_search": "Runs fast, filtered live-web lookups with domain and recency constraints.",
            "perplexity_ask": "Generates conversational AI responses grounded directly in real-time search context.",
            "perplexity_research": "Triggers Deep Research multi-step streaming pipelines for deep investigative topics.",
            "perplexity_reason": "Leverages advanced reasoning paths optimized for complex math, coding, or logic queries."
        }
    },

    "Stripe": {
        "description": "Interact with Stripe services over the Stripe API for finance and payments related tasks.",
        "tools": {
            "stripe_api_read": "Generically retrieves Stripe resources like Customers, Charges, Invoices, and Subscriptions.",
            "stripe_api_write": "Safely performs mutations such as creating checkout loops, issuing refunds, or updating subscriptions.",
            "search_stripe_documentation": "Queries the comprehensive Stripe documentation natively.",
            "stripe_implementation_planner": "Provides a guided, step-by-step checklist for configuring custom Stripe integration workflows."
        }
    },

    "Atlassian": {
        "description": "Tools for Atlassian products (Confluence and Jira). This integration supports both Atlassian Cloud and Jira Server/Data Center deployments.",
        "tools": {
            "jira_search": "Searches for Jira issues using Jira Query Language (JQL).",
            "jira_get_issue": "Retrieves the complete details, fields, and comments of a specific Jira issue.",
            "jira_create_issue": "Creates a new Jira issue with specified summaries, descriptions, and assignees.",
            "jira_update_issue": "Modifies the fields or attributes of an existing Jira issue.",
            "jira_transition_issue": "Changes the workflow status state of a Jira issue (e.g., To Do to In Progress).",
            "confluence_search": "Searches for Confluence pages, blogs, and attachments using Confluence Query Language (CQL).",
            "confluence_get_page": "Retrieves the body content and metadata of a specific Confluence page.",
            "confluence_create_page": "Publishes a new page to a specified Confluence space.",
            "confluence_add_comment": "Adds a comment to an existing Confluence page or blog post.",
            "read_teamwork_graph": "Maps out dependencies by reading linked external operational assets like active GitHub/Bitbucket PR deployments."
        }
    },

    "DeepWiki": {
        "description": "Tools for fetching and asking questions about GitHub repositories.",
        "tools": {
            "read_wiki_structure": "Extracts the complete documentation index or sitemap for an indexed GitHub repository.",
            "read_wiki_contents": "Retrieves the raw markdown contents of a specific repository documentation segment.",
            "ask_question": "Directly prompts an AI context-grounded interface about how the specific repository operates."
        }
    },

    "Fliesystem": {
        "description": "Local filesystem access with configurable allowed paths.",
        "tools": {
            "read_text_file": "Reads the text contents of a file within the allowed directory paths.",
            "read_media_file": "Reads and processes media file metadata or content streams safely.",
            "read_multiple_files": "Reads the contents of multiple specified files in a single operations block.",
            "write_file": "Creates a new file or completely overwrites an existing file with text content.",
            "edit_file": "Applies targeted, precise diff patches to modify parts of an existing file.",
            "create_directory": "Creates a new directory path inside the allowed filesystem limits.",
            "list_directory": "Lists the files and folders contained directly within a directory.",
            "list_directory_with_sizes": "Lists directory contents including exact file sizes and metadata details.",
            "directory_tree": "Generates a complete recursive visual tree map of folders and sub-files.",
            "move_file": "Moves or renames a file or directory from a source path to a destination path.",
            "search_files": "Performs a recursive regex pattern search across files in allowed directories.",
            "get_file_info": "Retrieves file metadata including size, creation date, and access permissions.",
            "list_allowed_directories": "Returns the explicit list of base directory paths the server is authorized to access."
        }
    }
}

