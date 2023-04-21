from pathlib import Path
from typing import Dict

from gql import gql
from graphql.language.ast import Document

def file_to_gql_documents(file_path: Path) -> Dict[str, Document]:
    """Return gql documents from a .graphql file.

    Read the file as text. Try to parse gql.Document objects.

    Returns:
        dict[str, Document]: { name: gql.Document }, where name is the gql operation name

    Example:
        query getMdfSignalIdByFileId($input: Int!) {
            mdf_signal(where: { mdf_signals_files: { file_id: { _eq: $input } } }) {
                id
            }
        }
        -->
        { "getMdfSignalIdByFileId": gql.Document }
    """
    with open(file_path, 'rt', encoding='UTF-8') as gql_text:
        test = gql(gql_text.read())
    ops = {}
    for definition in test.definitions:
        ops.update({definition.name.value: Document([definition])})
    return ops