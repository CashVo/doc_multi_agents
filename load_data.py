from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)

from llama_index.core.tools import QueryEngineTool, ToolMetadata

def load_data():
    # Load raw data
    print("Loading data...")
    document_names = [
        "api_content",
        "conceptual_content",
        "glossary_terms",
        "tutorial_content"
    ]
    document_content = {} # Stores the content of each doc
    document_indexes = {}
    query_engine_tools = []

    # Load indexes if it exists
    try:
        for doc in document_names:
            storage_context = StorageContext.from_defaults(
                persist_dir=f"./data/processed/{doc}"
            )
            document_indexes[doc] = load_index_from_storage(storage_context)

        index_loaded = True
        print("- Data loaded from existing indexes")
    except:
        index_loaded = False
        print("- No existing indexes found. Will attempt to load from raw files.")

    # If indexes does not already exists
    # Load raw content, create the index, and persist them to disk (for each document)
    print(f"* index_loaded = {index_loaded}")
    if not index_loaded:
        for doc in document_names:
            document_content[doc] = SimpleDirectoryReader(
                input_files=[f"./data/raw/{doc}" + (".json" if doc == "glossary_terms" else ".txt")]
            ).load_data()
            
            # build index
            document_indexes[doc] = VectorStoreIndex.from_documents(document_content[doc])

            # persist index
            document_indexes[doc].storage_context.persist(persist_dir=f"./data/processed/{doc}")
            print(f"- {doc}: Loaded and indexed")

    # Build indexes into engine tools
    for doc in document_names:
        doc_query_engine = document_indexes[doc].as_query_engine(similarity_top_k = 4)
        query_engine_tools.append(
            QueryEngineTool(
                query_engine = doc_query_engine,
                metadata=ToolMetadata(
                    name = doc,
                    description = (
                        f"Provide answers and information to the query about {doc} "
                        "Use a detailed plain text question as input to the tool"
                    )
                )
            )
        )

    print("Data loaded, indexed, and returing query engine tools object")
    return query_engine_tools