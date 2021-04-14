import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class ErrorType extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  error_type_id?: number;

  @property({
    type: 'string',
    required: true,
  })
  error_name: string;

  @property({
    type: 'string',
  })
  description?: string;

  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<ErrorType>) {
    super(data);
  }
}

export interface ErrorTypeRelations {
  // describe navigational properties here
}

export type ErrorTypeWithRelations = ErrorType & ErrorTypeRelations;
