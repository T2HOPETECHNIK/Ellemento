import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class State extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  state_id?: number;

  @property({
    type: 'number',
    required: true,
  })
  state_type_id: number;

  @property({
    type: 'number',
    required: true,
  })
  batch_id: number;

  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<State>) {
    super(data);
  }
}

export interface StateRelations {
  // describe navigational properties here
}

export type StateWithRelations = State & StateRelations;
